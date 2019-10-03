import os
import json
from datetime import datetime

hashtags = ["#videogames", "#gaming", "#nintendoswitch"]

start_date = datetime.fromtimestamp(1556686800).date()
end_date = datetime.fromtimestamp(1564721999).date()

NO_LIMIT_RANGE = False

def have_palindrome(post):
    for text in post.split():
        if text.isalpha():
            if len(text) > 1:
                if text == text[::-1]:
                    return text
    return "False"

data=os.listdir("data")
palindrome_posts={}
for hashtag in hashtags:
    palindrome_posts[hashtag]=[]
for file in data:
    if file.startswith("posts_"):
        with open("data/"+file,"r", encoding="utf-8") as data_file:
            posts = json.load(data_file)
            for post in posts:
                caption = post["caption"]
                url = "https://www.instagram.com/p/"+post["code"]
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
                        for hashtag in hashtags:
                            if hashtag in post_description:
                                palindrome = have_palindrome(post_description)
                                if palindrome != "False":
                                    post_description=post_description.replace("\n"," ")
                                    post_description=post_description.replace("\t"," ")
                                    post_description=post_description.replace("\r"," ")
                                    post_description=post_description.replace(","," ")

                                    palindrome_posts[hashtag].append(day+","+str(likes)+","+str(comments)+","+palindrome+","+post_description+","+url+"\n")
preppend = ""
if NO_LIMIT_RANGE:
    preppend = "../output_using_all_data/"

for hashtag in palindrome_posts.keys():
    if len(palindrome_posts[hashtag]) > 0:
        with open(preppend+"ej5_output/"+hashtag+"_palindrome"+".csv", "w", encoding="utf-8") as file:
            file.write("day,likes_number,comments_number,palindrome_found,post_description,url"+"\n")
            file.writelines(palindrome_posts[hashtag])
