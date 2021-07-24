import csv
import pickle
def get_time_of_vids():

    names = []
    swear = set()
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count+=1
            names.append(row[0])
    for name in names:
        id_time={}
        print(name + "\n")
        with open(name + "_Link.txt", "r", encoding="utf-8") as p_link:
            line_counter=0
            id_yt=""
            time=0
            for s in p_link:
                if s.find("https://youtu.be/")>-1:
                    id_yt = s[17:].rstrip()
                    line_counter += 1
                    continue
                line_counter += 1
                digit=s.split(" ")[0]
                if digit.isdigit():
                    time=int(digit)
                id_time[id_yt]=time
        a_file = open(name+"_dictionary_time.pkl", "wb")
        pickle.dump(id_time, a_file)
        a_file.close()
