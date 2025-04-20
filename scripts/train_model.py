import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

X_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train.values.ravel())

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
