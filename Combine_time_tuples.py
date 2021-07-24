import csv
import pickle
from collections import defaultdict
def combine():
    names = []
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count+=1
            names.append(row[0])
    #combining time and count into 1 dictionary
    month_count_time=defaultdict(dict)
    for name in names:
        a_file = open(name+"_new_tuple.pkl", "rb")
        date_id_count = pickle.load(a_file)
        a_file = open(name + "_dictionary_time.pkl", "rb")
        id_time = pickle.load(a_file)
        for date,id_yt,count in date_id_count:
            if id_time.get(id_yt,0)==0:
                continue
            year=date[:4]
            month_count_time[year]["count"]=month_count_time[year].get("count",0)+count
            month_count_time[year]["time"]=month_count_time[year].get("time",0)+id_time[id_yt]
    a_file = open( "Complete_dictionary2.pkl", "wb")
    pickle.dump(month_count_time, a_file)
    a_file.close()