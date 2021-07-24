import csv
import string
import pickle

def count_swear_words(file_swear_words):
    names = []
    swear = set()
    #gets a predetermined file of swear words
    with open(file_swear_words, "r", encoding="utf-8") as swearWords:
        for s in swearWords:
            swear.add(s.rstrip())
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0

        for row in csv_reader:
            line_count+=1
            names.append(row[0])
    for name in names:
        id_swear={}
        print(name + "\n")
        with open(name + "_Link.txt", "r", encoding="utf-8") as p_link:
            line_counter=0
            id_yt=""
            without_asterik = string.punctuation[:9] + string.punctuation[10:]
            for s in p_link:
                line_counter += 1
                if s.find("https://youtu.be/")>-1:
                    id_yt=s[17:].rstrip()
                    continue
                count=s.count("[ __ ]")
                s = s.translate(str.maketrans('', '', without_asterik))
                s = s.rstrip()
                s = s.lower()
                for word in s.split(" "):
                    if word in swear:
                        count+=1
                        continue
                    #checks if a combination of swear words exist
                    for w in ["fuck","shit","pussy","bitch","bastard","damn"]:
                        if word.find(w)!=-1:
                            count+=1
                            break
                id_swear[id_yt]=id_swear.get(id_yt,0)+count
        a_file = open(name+"_dictionary.pkl", "wb")
        pickle.dump(id_swear, a_file)
        a_file.close()
