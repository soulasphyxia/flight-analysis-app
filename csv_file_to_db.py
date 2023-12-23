import pandas as pd
from pycaret.regression import *
import sqlite3

conn = sqlite3.connect('data_base_flight.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM flight_price')


data = cursor.fetchall()

conn.close()

models = setup_for_model = setup(data, target ='Price',use_gpu=True,normalize = True,normalize_method='robust')
xgbooster = create_model('xgboost')
tune_xgb = tune_model(xgbooster,choose_better = True)
save_model(tune_xgb, "model_prodaction")