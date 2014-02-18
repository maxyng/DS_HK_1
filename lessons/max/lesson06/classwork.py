import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model,feature_selection

cars = pd.read_csv('./../../../data/cars93.csv')
cars_numeric = cars._get_numeric_data()
cars_numeric.fillna(0)

feature_selection.univariate_selection.f_regression(cars_numeric.dropna
()['EngineSize'],cars_numeric.dropna())
