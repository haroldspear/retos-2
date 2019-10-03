import os
import json
from datetime import datetime
import emoji
import calendar
import sys
import argparse

parser = argparse.ArgumentParser(description='Obtiene el top 20 de handles que postearon cada # por año, mes y día' )
parser.add_argument('-nl', '--nolimit', dest='limit', help='--nolimit True, desabilita el limite entre el rango de fechas y la salida, se va a output_using_all_data', default="False")
args = parser.parse_args(sys.argv[1:])

NO_LIMIT_RANGE = False
DATASET_FOLDER = "../data"
OUTPUT_FOLDER = "ej4_output"

YEAR_DATA = 2019

OUTPUT_ALL_DATA_FOLDER = "../output_using_all_data/"

if args.limit == "True":
    NO_LIMIT_RANGE = True

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

hashtags = ["#videogames", "#gaming", "#nintendoswitch"]

start_date = datetime.fromtimestamp(1556686800).date()
end_date = datetime.fromtimestamp(1564721999).date()
months = {}

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

data=os.listdir(DATASET_FOLDER)

for file in data:
    if file.startswith("posts_"):
        with open(DATASET_FOLDER+"/"+file,"r", encoding="utf-8") as data_file:
            posts = json.load(data_file)
            for post in posts:
                caption = post["caption"]
                timestamp = post["taken_at"]
                date_time = datetime.fromtimestamp(timestamp)
                date = date_time.date()
                if start_date <= date <= end_date or (NO_LIMIT_RANGE and date.year==YEAR_DATA):
                    if date.month not in months.keys():
                        months[date.month] = {}
                        for hashtag in hashtags:
                            months[date.month][hashtag]=[]
                    if caption!=None:
                        post_description=caption["text"]
                        for hashtag in hashtags:
                            if hashtag in post_description:
                                post_description=post_description.replace("\n"," ")
                                post_description=post_description.replace("\t"," ")
                                post_description=post_description.replace("\r"," ")
                                post_description=post_description.replace(","," ")
                                hashtags_post = get_hastags(post_description)
                                for htg in hashtags_post:
                                    if htg not in months[date.month][hashtag]:
                                        months[date.month][hashtag].append(htg+"\n")

preppend = ""
if NO_LIMIT_RANGE:
    preppend = OUTPUT_ALL_DATA_FOLDER
    if not os.path.exists(preppend):
        os.makedirs(preppend)
    if not os.path.exists(preppend+OUTPUT_FOLDER):
        os.makedirs(preppend+OUTPUT_FOLDER)

for month in months.keys():
    month_name = calendar.month_name[month]
    for hashtag_1 in hashtags:
        #No repetir par de hashtags
        start = False
        for hashtag_2 in hashtags:
            if start:
                overlap = list(set(months[month][hashtag_1]) & set(months[month][hashtag_2]))
                if len(overlap) >0:
                    with open(preppend+OUTPUT_FOLDER+"/"+hashtag_1+"_"+hashtag_2+"_"+month_name+".csv", "w", encoding="utf-8") as file:
                        file.write("hastags_overlapped\n")
                        file.writelines(overlap)

            if hashtag_1 == hashtag_2:
                start = True
