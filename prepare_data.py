import pandas as pd


def prepare_data(data):
    data['Routes'] = data['Route'].str.count('→')
    data.drop(['Route','Dep_Time','Duration','Arrival_Time'],1,inplace =True)
    data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'])
    return data
    