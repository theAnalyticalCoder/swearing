
import pickle
import pandas as pd
def interpret():
    #calculates the average per hour
    a_file = open("Complete_dictionary2.pkl", "rb")
    complete_dict = pickle.load(a_file)
    a_file.close()
    p=pd.DataFrame(complete_dict)
    p.loc['Average'] = p.loc['count'] / (p.loc['time']/3600)
    #could be printed out or could do manipulations in context
    p.to_csv('Average.csv')
