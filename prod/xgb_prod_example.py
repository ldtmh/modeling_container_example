import numpy as np
import pickle
from sklearn.datasets import  load_diabetes
from sklearn.metrics import  mean_squared_error
from numpy import savetxt

file_name = "/app/xgb_reg.pkl"

xgb_model_loaded = pickle.load(open(file_name, "rb"))

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

y_pred = xgb_model_loaded.predict(X)

mse=mean_squared_error(y, y_pred)

print(np.sqrt(mse))

savetxt('/output/predictions.csv', y_pred, delimiter=',')