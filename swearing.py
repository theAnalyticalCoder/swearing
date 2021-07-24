import csv
import pickle
from pyyoutube import Api

def get_dates(Api_key):
#getting the dates
    names=[]
    api = Api(api_key=Api_key)
    with open('YoutubeChannels.csv') as yt_Channels:
        csv_reader = csv.reader(yt_Channels, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 10:
                break
            line_count+=1
            names.append(row[0])
    for name in names:
        id_swear=[]
        line_count=0
        print(name + "\n")
        a_file = open(name+"_dictionary.pkl", "rb")
        output = pickle.load(a_file)
        for key,val in output.items():

            line_count+=1
            try:
                video_by_id = api.get_video_by_id(video_id=key)
            except:
                print("Api Key not working on"+name)
                a_file = open(name + "_new_tuple.pkl", "wb")
                pickle.dump(id_swear, a_file)
                a_file.close()
                exit(-1)

            date=video_by_id.items[0].snippet.publishedAt
            id_swear.append((date[:10],key,val))
        a_file = open(name + "_new_tuple.pkl", "wb")
        pickle.dump(id_swear, a_file)
        a_file.close()


