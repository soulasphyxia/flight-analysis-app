import pandas as pd
from pycaret.regression import *
from prepare_data import prepare_data

data_set =pd.read_pickle('dataset_for_model.pkl')
data = prepare_data(data_set)

models = setup(data, target ='Price')
best = compare_models()
tune_model = tune_model(best)
blender = blend_models([best,tune_model])

save_model(blender, "model_prodact")