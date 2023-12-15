from random import randint
import pandas as pd
from pycaret.regression import *
import numpy




def get_num(airline, date, source, destination, total_stops, additional_info, route):
    data = {
        'Airline': [airline],
        'Date_of_Journey': [date],
        'Source': [source],
        'Destination': [destination],
        'Total_Stops': [total_stops],
        'Additional_Info': [additional_info],
        'Routes': [route]
    }
    
    df = pd.DataFrame(data)
    data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'])
    model = load_model('model_prodaction')
    x = int(model.predict(data)[0])
    return x
