import os
import json
import collections
from datetime import datetime
import sys
import argparse

parser = argparse.ArgumentParser(description='Obtiene el top 20 de handles que postearon cada # por año, mes y día' )
parser.add_argument('-nl', '--nolimit', dest='limit', help='--nolimit True, desabilita el limite entre el rango de fechas y la salida, se va a output_using_all_data', default="False")
args = parser.parse_args(sys.argv[1:])

NO_LIMIT_RANGE = False

if args.limit == "True":
    NO_LIMIT_RANGE = True

DATASET_FOLDER = "../data"
OUTPUT_FOLDER = "ej3_output"

OUTPUT_ALL_DATA_FOLDER = "../output_using_all_data/"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
if not os.path.exists(OUTPUT_FOLDER+"/days"):
    os.makedirs(OUTPUT_FOLDER+"/days")
if not os.path.exists(OUTPUT_FOLDER+"/months"):
    os.makedirs(OUTPUT_FOLDER+"/months")
if not os.path.exists(OUTPUT_FOLDER+"/years"):
    os.makedirs(OUTPUT_FOLDER+"/years")

top = 20
handles = {}
hashtags = ["#videogames", "#gaming", "#nintendoswitch"]

start_date = datetime.fromtimestamp(1556686800).date()
end_date = datetime.fromtimestamp(1564721999).date()

days = {}
months = {}
years = {}

data=os.listdir(DATASET_FOLDER)
for file in data:
    if file.startswith("posts_"):
        with open(DATASET_FOLDER+"/"+file,"r", encoding="utf-8") as data_file:
            posts = json.load(data_file)
            for post in posts:
                caption = post["caption"]
                timestamp = post["taken_at"]
                date_time = datetime.fromtimestamp(timestamp)
                day = str(date_time.strftime("%d-%m-%Y"))
                month = str(date_time.strftime("%m-%Y"))
                year = str(date_time.strftime("%Y"))

                date = date_time.date()
                if start_date <= date <= end_date or NO_LIMIT_RANGE:

                    if day not in days.keys():
                        days[day] = {}
                        for hashtag in hashtags:
                            days[day][hashtag] = {}
                    if month not in months.keys():
                        months[month] = {}
                        for hashtag in hashtags:
                            months[month][hashtag] = {}
                    if year not in years.keys():
                        years[year] = {}
                        for hashtag in hashtags:
                            years[year][hashtag] = {}
                    if caption!=None:
                        post_description=caption["text"]
                        user = post["user"]["username"]
                        for hashtag in hashtags:
                            if hashtag in post_description:
                                if user not in days[day][hashtag].keys():
                                    days[day][hashtag][user] = 1
                                else:
                                    days[day][hashtag][user] = days[day][hashtag][user] + 1

                                if user not in months[month][hashtag].keys():
                                    months[month][hashtag][user] = 1
                                else:
                                    months[month][hashtag][user] = months[month][hashtag][user] + 1

                                if user not in years[year][hashtag].keys():
                                    years[year][hashtag][user] = 1
                                else:
                                    years[year][hashtag][user] = years[year][hashtag][user] + 1


top_users_days = {}
top_users_months = {}
top_users_years = {}
for day in days.keys():
    #for day in days.keys():
    top_users_days[day] = {}
    for hashtag in hashtags:
        days[day][hashtag] = collections.OrderedDict(sorted(days[day][hashtag].items(), key=lambda x: x[1], reverse=True))
        top_users_days[day][hashtag] = []
        count=0
        for user, posts_count in days[day][hashtag].items():
            if count == top:
                break
            else:
                top_users_days[day][hashtag].append(user+","+str(posts_count)+"\n")
            count+=1

for month in months.keys():
    #for hashtag in hashtags:
    top_users_months[month] = {}
    for hashtag in hashtags:
        months[month][hashtag] = collections.OrderedDict(sorted(months[month][hashtag].items(), key=lambda x: x[1], reverse=True))
        top_users_months[month][hashtag] = []
        count=0
        for user, posts_count in months[month][hashtag].items():
            if count == top:
                break
            else:
                top_users_months[month][hashtag].append(user+","+str(posts_count)+"\n")
            count+=1

for year in years.keys():
    #for hashtag in hashtags:
    top_users_years[year] = {}
    for hashtag in hashtags:
        years[year][hashtag] = collections.OrderedDict(sorted(years[year][hashtag].items(), key=lambda x: x[1], reverse=True))
        top_users_years[year][hashtag] = []
        count=0
        for user, posts_count in years[year][hashtag].items():
            if count == top:
                break
            else:
                top_users_years[year][hashtag].append(user+","+str(posts_count)+"\n")
            count+=1

preppend = ""
if NO_LIMIT_RANGE:
    preppend = OUTPUT_ALL_DATA_FOLDER
    if not os.path.exists(preppend):
        os.makedirs(preppend)
    if not os.path.exists(preppend+OUTPUT_FOLDER):
        os.makedirs(preppend+OUTPUT_FOLDER)
    if not os.path.exists(preppend+OUTPUT_FOLDER+"/days"):
        os.makedirs(preppend+OUTPUT_FOLDER+"/days")
    if not os.path.exists(preppend+OUTPUT_FOLDER+"/months"):
        os.makedirs(preppend+OUTPUT_FOLDER+"/months")
    if not os.path.exists(preppend+OUTPUT_FOLDER+"/years"):
        os.makedirs(preppend+OUTPUT_FOLDER+"/years")

for day in top_users_days.keys():
    for hashtag in hashtags:
        if hashtag in top_users_days[day].keys():
            if len(top_users_days[day][hashtag]) > 0:
                with open(preppend+OUTPUT_FOLDER+"/days/top_"+str(top)+"_"+hashtag+"_"+day+".csv", "w", encoding="utf-8") as top_file:
                    top_file.writelines(top_users_days[day][hashtag])

for month in top_users_months.keys():
    for hashtag in hashtags:
        if hashtag in top_users_months[month].keys():
            if len(top_users_months[month][hashtag]) > 0:
                with open(preppend+OUTPUT_FOLDER+"/months/top_"+str(top)+"_"+hashtag+"_"+month+".csv", "w", encoding="utf-8") as top_file:
                    top_file.writelines(top_users_months[month][hashtag])

for year in top_users_years.keys():
    for hashtag in hashtags:
        if hashtag in top_users_years[year].keys():
            if len(top_users_years[year][hashtag]) > 0:
                with open(preppend+OUTPUT_FOLDER+"/years/top_"+str(top)+"_"+hashtag+"_"+year+".csv", "w", encoding="utf-8") as top_file:
                    top_file.writelines(top_users_years[year][hashtag])
