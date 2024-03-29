from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import json
import collections

analyser = SentimentIntensityAnalyzer()

DATASET_FOLDER = "../data"
OUTPUT_FOLDER = "ej1_output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

POSITIVE = "pos"
NEGATIVE = "neg"
NEUTRAL = "neu"
positive_count = 0
negative_count = 0
neutral_count = 0
hashtag_count_pos = 0
hashtag_count_neg = 0
hashtag_count_neu = 0
def score_sentiment(post):
    global positive_count
    global negative_count
    global neutral_count

    global hashtag_count_pos
    global hashtag_count_neg
    global hashtag_count_neu
    score = analyser.polarity_scores(post)
    score.pop("compound")
    score = collections.OrderedDict(sorted(score.items(), key=lambda x: x[1], reverse=True))
    sentiment = next(iter(score))
    if sentiment == POSITIVE:
        positive_count += 1
        hashtag_count_pos += 1
    elif sentiment == NEGATIVE:
        negative_count += 1
        hashtag_count_neg += 1
    elif sentiment == NEUTRAL:
        neutral_count += 1
        hashtag_count_neu += 1

data=os.listdir(DATASET_FOLDER)
for file in data:
    if file.startswith("comments_"):
        hashtag = file.split("_")[1].split(".")[0]
        hashtag_count_pos = 0
        hashtag_count_neg = 0
        hashtag_count_neu = 0
        with open(DATASET_FOLDER+"/"+file,"r",encoding="utf-8") as data_file:
            comments = data_file.readlines()
            for comment in comments:
                score_sentiment(comment)
    with open(OUTPUT_FOLDER+"/"+hashtag+".csv","w") as ejercicio1:
        ejercicio1.write("positive_posts, negative_posts, neutral_posts\n")
        ejercicio1.write(str(hashtag_count_pos) + "," + str(hashtag_count_neg) + "," + str(hashtag_count_neu)+"\n")


with open(OUTPUT_FOLDER+"/sentiments_posts.csv","w") as ejercicio1:
    ejercicio1.write("positive_posts, negative_posts, neutral_posts\n")
    ejercicio1.write(str(positive_count) + "," + str(negative_count) + "," + str(neutral_count)+"\n")
