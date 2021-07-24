
import csv
import string
def swear_words(file):
    names = []
    swear_words = set()
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0

        for row in csv_reader:
            line_count+=1
            names.append(row[0])
    for name in names:

        with open(name + "_Text.txt", "r", encoding="utf-8") as p_text:
            line_counter=0
            for s in p_text:
                line_counter+=1
                #removes all punctuation save the asteriks
                without_asterik=string.punctuation[:9]+string.punctuation[10:]
                s = s.translate(str.maketrans('', '', without_asterik))
                s = s.rstrip()
                s = s.lower()
                for word in s.split(" "):
                    if '*' in word:
                        swear_words.add(word)
    with open(file, "a", encoding="utf-8") as words:
        for x in swear_words:
            words.write(x + "\n")