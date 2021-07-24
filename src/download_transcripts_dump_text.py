# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from youtube_transcript_api import YouTubeTranscriptApi
from pyyoutube import Api
from yt_videos_list import ListCreator
import re
import csv
import io
def get_video_url(channel):

    lc = ListCreator(driver='chrome', scroll_pause_time=0.8)
    l=lc.create_list_for(url=channel)


def dump():
    names=[]
    error_yt=open('Errors.txt', "a")
    #gets the names of the channel then creates a list of all their videos
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0

        for row in csv_reader:
            names.append(row[0])
            video = row[1]
            line_count+=1
            try:
                get_video_url(video)
            except:
                error_yt.write(video+" is incorrect")
                continue



    for name in names:
        try:
            with open(name+'_reverse_chronological_videos_list.csv', encoding='utf8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0

                #open two text files one only the text the other with the times and the links

                with open(name+"_Text.txt", "a", encoding="utf-8") as p_text:
                    with open(name+"_Link.txt", "a", encoding="utf-8") as p_link:

                        for row in csv_reader:
                            if line_count==0 :
                                line_count += 1
                                continue
                            #gets the Id of the yt vid
                            id_yt = row[2][row[2].index("=")+1:]
                            line_count += 1
                            print(name+" line "+str(line_count-1))
                            try:
                                #gets the transcript
                                transcript_list = YouTubeTranscriptApi.list_transcripts(id_yt)
                                dictionary = YouTubeTranscriptApi.get_transcript(id_yt)
                            except:
                                print("error")
                                continue
                            p_link.write("https://youtu.be/"+id_yt+"\n")
                            for d in dictionary:
                                #we will make a set of all the swear words so having a text file of just words is helpful
                                p_text.write(d['text']+"\n")
                                p_link.write(str(int(d['start']))+" "+d['text']+"\n")
        except:
            error_yt.write(name + " is incorrect")
            continue
