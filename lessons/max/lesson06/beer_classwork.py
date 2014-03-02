import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import re

beer = pd.read_csv('./../../../data/1.txt', delimiter="\t")
beer = beer.dropna()
def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

beer['Good'] = beer['WR'].apply(good)

logm = linear_model.LinearRegression()
input = beer[ ['Reviews', 'ABV'] ].values
good = beer['Good'].values
logm.fit(input, good)
logm.predict(input)
logm.score(input, good)

beer_type = ['Ale', 'Stout', 'IPA', 'Lager']

for t in beer_type:
	beer[t] = beer['Type'].str.contains(t) * 1

input = beer[ ['Ale', 'Stout', 'IPA', 'Lager'] ].values
y = beer['Good'].values

logm.fit(input, y)
logm.predict(input)
logm.score(input,y)

logm.set_params(penalty = 'l1')