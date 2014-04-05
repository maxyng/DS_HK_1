import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm,neighbors, datasets, feature_selection
import re

n_neighbors = range(1, 101, 2)

beer = pd.read_csv('./../../../data/1.txt', delimiter="\t")
beer = beer.dropna()
def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

beer['Good'] = beer['WR'].apply(good)

beer = beer.drop('Rank',1)
beer = beer.drop('Name',1)
beer = beer.drop('Brewery',1)
beer = beer.drop('Type',1)
numForTraining = len(beer) * 0.7

trainingSet_X = beer[:numForTraining]
testSet_X = beer[numForTraining:]

trainingSet_Y = trainingSet_X['Good']
testSet_Y = testSet_X['Good']

trainingSet_X.drop('Good',1)
testSet_X.drop('Good',1)


scores = []
for n in n_neighbors:
    clf = svm.SVN()
    clf.fit(trainingSet_X, trainingSet_Y)    
    scores.append(clf.score(testSet_X, testSet_Y))


plt.plot(n_neighbors, scores)
plt.show()

