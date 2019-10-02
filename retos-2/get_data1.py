from InstagramAPI import InstagramAPI as iApi
import random
from time import sleep
import json

api = iApi("haroldapiinstagram@gmail.com","instagramapi44")
api.login()
next_max_id =""
current_date = 99999999999999
end_date = 1556686800000
start_date = 1564721999000
#videogames,#gaming,# nintendoswitch
hashtags = ["videogames"]
count = 1
posts = []
comments_count = 1
comments = []
count_iter=1
for hashtag in hashtags:
    with open("data/comments_"+hashtag+".txt", "w", encoding="utf-8") as comments_file:
        comments_file.write("")
    while True :
        try:
            print(count,comments_count)
            feed = api.getHashtagFeed(hashtag, next_max_id)
            temp = api.LastJson
            """last_item = len(temp["items"])-1
            last_item_date = temp["items"][last_item]["taken_at"]*1000
            print(last_item_date)
            if last_item_date >= start_date:
                current_date = last_item_date
                sleep(random.randint(1,3))
                next_max_id = temp["next_max_id"]
                continue"""
            print(next_max_id)
            for post in temp["items"]:
                current_date = post["taken_at"]*1000
                #if current_date <= start_date:
                posts.append(post)
                if count >= 500:
                    with open("data/posts_"+hashtag+"_"+str(count_iter)+".json", "w", encoding="utf-8") as posts_json:
                        json.dump(posts, posts_json)
                        posts = []
                        count_iter+=1
                        count=0
                count+=1

                has_more_comments=post.get("has_more_comments", False)
                post_id = str(post["pk"])
                max_comment_id = ""
                while has_more_comments:
                    feed_comments = api.getMediaComments(post_id, max_id=max_comment_id)

                    for comment in api.LastJson['comments']:
                        comment_text=comment["text"]
                        comment_text=comment_text.replace("\n"," ")
                        comment_text=comment_text.replace("\t"," ")
                        comment_text=comment_text.replace("\r"," ")
                        comment_text=comment_text.replace(","," ")
                        comments.append(comment_text+"\n")
                        comments_count+=1

                    if comments_count >= 100:
                        with open("data/comments_"+hashtag+".txt", "a", encoding="utf-8") as comments_file:
                            comments_file.writelines(comments)
                            comments = []
                            comments_count=0

                    has_more_comments = api.LastJson.get('has_more_comments',False)

                    if has_more_comments:
                        max_comment_id = api.LastJson['next_max_id']
                        random.randint(1,3)

            sleep(random.randint(10,15)+count%random.randint(1,2))
            next_max_id = temp["next_max_id"]
        except Exception as e:
            print("Error")
            print(e)

    print("Exit")
    if len(posts) > 0:
        with open("data/posts_"+hashtag+"_end"+".json", "w", encoding="utf-8") as posts_json:
            json.dump(posts, posts_json)

            api = iApi("haroldapiinstagram@gmail.com","instagramapi44")
            hashtags = ["videogames"]
