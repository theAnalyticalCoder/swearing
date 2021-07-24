import download_transcripts_dump_text as dp
import Combine_time_tuples as cb
import Interpret_Data as Inter
import get_swear_words as swear
import get_time as time
import get_num_swears_pickle as swear_count
import swearing as dates
if __name__ == '__main__':
    '''
    gets the transcripts and dumps them into two files
    1. Text file containing only the Text which will be used to find the unique swear words
    2. Text file containing the text and the youtube link+time
    '''
    dp.dump()
    '''
    parses the text files for any word containg an asteriks as youtube does not have a standard way of censoring
    ex shit== sh*t, sh**, sh****** etc
    unfortunately this file needs to be parsed by hand because there are many different iterations that are unexpected
    '''
    swear.swear_words("Swear_Words.txt")
    '''uses the file of potential swear words generated above plus adds in any swear words that could slip by 
    e.g absofuckinglutely
    '''
    swear_count.count_swear_words("Swear_Words_Parsed.txt")
    '''
    Gets the dates of the videos using an API key
    '''
    dates.get_dates("Api_Key_Needed")
    '''
    I realized halfway through that I forgot to get the length of the videos
    so I reparsed the Link files to get the length of each Video
    '''

    time.get_time_of_vids()
    ''' Combines the time with date/id/swear count tuple separting by year'''
    cb.combine()
    '''
    A file that could be used to interpret the data
    I just outputed the data to an excel file and made my graph there '''
    Inter.interpret()
