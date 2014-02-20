import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model,feature_selection

cars = pd.read_csv('./../../../data/cars93.csv')
cars_numeric = cars._get_numeric_data()
cars_mpg_city = cars_numeric['MPG.city']
cars_mpg_highway = cars_numeric['MPG.highway']

cars_numeric = cars_numeric.drop(['MPG.highway','MPG.city'],1)
cars_numeric = cars_numeric.fillna(0)

result = feature_selection.univariate_selection.f_regression(cars_numeric.dropna(),cars_mpg_city)


zip(cars_numeric.columns.values,result[1])
fp = zip(result[1],cars_numeric.columns.values)
sorted(fp)