import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

baseball_stats = pd.read_csv('./../../../data/baseball.csv')

baseball_stats_filter = baseball_stats[ ["HR", "RBI", 'R', "G", "SB", "salary", 'height', 'weight', 'yearID'] ]

salary = baseball_stats_filter['salary']
baseball_stats_filter = baseball_stats_filter.drop('salary',1)

baseball_stats_filter = baseball_stats_filter.fillna(0)

result = feature_selection.univariate_selection.f_regression(baseball_stats_filter,salary)
