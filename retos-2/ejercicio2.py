# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime
import emoji
import re
import calendar
import pandas
import matplotlib.pyplot as plt
import collections
import matplotlib

hashtags = ["#videogames", "#gaming", "#nintendoswitch"]

start_date = datetime.fromtimestamp(1556686800).date()
end_date = datetime.fromtimestamp(1564721999).date()
months = {}

data=os.listdir("data")

for file in data:
    if file.startswith("posts_"):
        with open("data/"+file,"r", encoding="utf-8") as data_file:
            posts = json.load(data_file)
            for post in posts:
                caption = post["caption"]
                timestamp = post["taken_at"]
                date_time = datetime.fromtimestamp(timestamp)
                date = date_time.date()
                if start_date <= date <= end_date:
                    if date.month not in months.keys():
                        months[date.month] = {}
                        for hashtag in hashtags:
                            months[date.month][hashtag]={}
                    if caption!=None:
                        post_description=caption["text"]
                        for hashtag in hashtags:
                            if hashtag in post_description:
                                allchars = [str for str in post_description]
                                emojis_in_post = [c for c in allchars if c in emoji.UNICODE_EMOJI]
                                for emoji_ in emojis_in_post:
                                    #emoji_ = emoji_.encode().decode('utf-8')
                                    if emoji_ in months[date.month][hashtag].keys():
                                        months[date.month][hashtag][emoji_] = months[date.month][hashtag][emoji_] + 1
                                    else:
                                        months[date.month][hashtag][emoji_] = 1
for month in months.keys():
    month_name = calendar.month_name[month]
    for hashtag in hashtags:
        if len(months[month][hashtag]) > 0:
            months[month][hashtag] = collections.OrderedDict(sorted(months[month][hashtag].items(), key=lambda x: x[1], reverse=True))
            with open("ej2_output/frecuencias_"+hashtag+"_"+month_name+".csv", "w", encoding="utf-8") as file:
                file.write("Emoji, Frecuencia\n")
                for emoj, freq in months[month][hashtag].items():
                    file.write(emoj+","+str(freq)+"\n")

            top = 10
            count=0
            dataframe_dict = {}
            dataframe_dict["Emojis"] = []
            dataframe_dict["Frecuencia"] = []
            for k, v in months[month][hashtag].items():
                if count == top:
                    break
                else:
                    dataframe_dict["Emojis"].append(k)
                    dataframe_dict["Frecuencia"].append(v)
                count+=1
            df = pandas.DataFrame.from_dict(dataframe_dict)
            ax = df.plot(kind='bar')
            #plt.figure()
            locs, labels=plt.xticks()
            plt.xlabel("Emojis")
            plt.ylabel("Frecuencias")
            plt.suptitle("Histograma de "+hashtag+ " en "+ month_name)
            plt.xticks(locs,dataframe_dict["Emojis"], horizontalalignment='right')
            #plt.show()
            #count = 0
            #ax.set_xticks(dataframe_dict["Emojis"])
            #for i in ax.patches:
            #    ax.text(i.get_width()+.3, i.get_y()+.38, dataframe_dict["Emojis"][count], fontsize=15,color='dimgrey')
            #    count+=1

            plt.savefig("ej2_output/"+hashtag+"_"+month_name+'.png', format='png')


print(months.keys())
