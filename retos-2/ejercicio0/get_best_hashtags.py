import os
import json
from datetime import datetime
import emoji
import collections
import sys
import argparse

parser = argparse.ArgumentParser(description='Obtiene el top 20 de handles que postearon cada # por año, mes y día' )
parser.add_argument('-nl', '--nolimit', dest='limit', help='--nolimit True, desabilita el limite entre el rango de fechas y la salida, se va a output_using_all_data', default="False")
args = parser.parse_args(sys.argv[1:])

NO_LIMIT_RANGE = False
DATASET_FOLDER = "../data"
OUTPUT_FOLDER = "ej0_output"

OUTPUT_ALL_DATA_FOLDER = "../output_using_all_data/"

if args.limit == "True":
    NO_LIMIT_RANGE = True

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

TOP_BEST_HASHTAGS = 100

hashtags_default = ["#videogames", "#gaming", "#nintendoswitch"]

start_date = datetime.fromtimestamp(1556686800).date()
end_date = datetime.fromtimestamp(1564721999).date()

data=os.listdir(DATASET_FOLDER)

hashtags={}

hashtag_dict = {
    "posts_number": 0,
    "likes_number": 0,
    "comments_number": 0,
    "likes_post_relation": 0,
    "comments_post_relation": 0
}


def get_hastags(post):
    hashtags_in_post = []
    for text in post.split():
        if len(text) > 1:
            if text.startswith("#"):
                hashtag = text[1:]
                allchars = [str for str in hashtag]
                is_hashtag = True
                for c in allchars:
                    if not c.isalpha() and c not in emoji.UNICODE_EMOJI:
                        is_hashtag = False
                if is_hashtag:
                    hashtags_in_post.append(text)

    return hashtags_in_post


for file in data:
    if file.startswith("posts_"):
        with open(DATASET_FOLDER+"/"+file,"r", encoding="utf-8") as data_file:
            posts = json.load(data_file)
            for post in posts:
                caption = post["caption"]
                likes = post.get("like_count",0)
                comments = post.get("comment_count",0)
                timestamp = post["taken_at"]
                date_time = datetime.fromtimestamp(timestamp)
                day = str(datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y"))
                date = date_time.date()
                #Limit range date
                if start_date <= date <= end_date or NO_LIMIT_RANGE:
                    if caption!=None:
                        post_description=caption["text"]
                        post_description=post_description.replace("\n"," ")
                        post_description=post_description.replace("\t"," ")
                        post_description=post_description.replace("\r"," ")
                        post_description=post_description.replace(","," ")
                        hashtags_post = get_hastags(post_description)
                        #No repetir por post
                        current_post = []
                        for htg in hashtags_post:
                            if htg not in current_post:
                                current_post.append(htg)
                                if htg not in hashtags_default:
                                    if htg in hashtags:
                                        hashtags[htg]["posts_number"] = hashtags[htg]["posts_number"] + 1
                                        hashtags[htg]["likes_number"] = hashtags[htg]["likes_number"] + likes
                                        hashtags[htg]["comments_number"] = hashtags[htg]["comments_number"] + comments
                                    else:
                                        hashtags[htg] = hashtag_dict.copy()
                                        hashtags[htg]["posts_number"] = 1
                                        hashtags[htg]["likes_number"] = likes
                                        hashtags[htg]["comments_number"] = comments

#Get hashtag with more likes and comments, and relation likes/post (likes x post) - comments/post (comments x post)
for hashtag, hashtag_dict in hashtags.items():
    hashtags[hashtag]["likes_post_relation"] = hashtag_dict["likes_number"] / hashtag_dict["posts_number"]
    hashtags[hashtag]["comments_post_relation"] = hashtag_dict["comments_number"] / hashtag_dict["posts_number"]

preppend = ""
if NO_LIMIT_RANGE:
    preppend = OUTPUT_ALL_DATA_FOLDER
    if not os.path.exists(preppend):
        os.makedirs(preppend)
    if not os.path.exists(preppend+OUTPUT_FOLDER):
        os.makedirs(preppend+OUTPUT_FOLDER)

hashtags = collections.OrderedDict(sorted(hashtags.items(), key=lambda x: x[1]["likes_post_relation"], reverse=True))

count=0
best_hastags_likes = []
for hashtag,likes in hashtags.items():
    if count == TOP_BEST_HASHTAGS:
        break
    else:
        best_hastags_likes.append(hashtag+","+str(hashtags[hashtag]["likes_post_relation"])+","+str(hashtags[hashtag]["likes_number"])+","+str(hashtags[hashtag]["posts_number"])+"\n")
    count+=1
with open(preppend+OUTPUT_FOLDER+"/"+"best_hastags_to_get_likes"+".csv","w",encoding="utf-8") as file:
    file.write("hashtag,likes_post_relation,likes_number,posts_number\n")
    file.writelines(best_hastags_likes)

count=0
best_hashtags_comments = []
hashtags = collections.OrderedDict(sorted(hashtags.items(), key=lambda x: x[1]["likes_post_relation"], reverse=True))
for hashtag,comments in hashtags.items():
    if count == TOP_BEST_HASHTAGS:
        break
    else:
        best_hashtags_comments.append(hashtag+","+str(hashtags[hashtag]["comments_post_relation"])+","+str(hashtags[hashtag]["comments_number"])+","+str(hashtags[hashtag]["posts_number"])+"\n")
    count+=1
with open(preppend+OUTPUT_FOLDER+"/"+"best_hastags_to_get_comments"+".csv","w",encoding="utf-8") as file:
    file.write("hashtag,comments_post_relation,comments_number,posts_number\n")
    file.writelines(best_hashtags_comments)
