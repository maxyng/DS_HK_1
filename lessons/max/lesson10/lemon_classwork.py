import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, cross_validation

lemon_training = pd.read_csv('C:\datascience\data\class\lemonsClassificationData\lemon_training.csv')
lemon_training =lemon_training.fillna(0)

isBad = lemon_training['IsBadBuy']
lemon_training = lemon_training.drop('RefId',1)
lemon_training = lemon_training.drop('IsBadBuy',1)
lemon_training = lemon_training.drop('PurchDate',1)
lemon_training = lemon_training.drop('Auction',1)
lemon_training = lemon_training.drop('Make',1)
lemon_training = lemon_training.drop('Model',1)
lemon_training = lemon_training.drop('Trim',1)
lemon_training = lemon_training.drop('SubModel',1)
lemon_training = lemon_training.drop('Color',1)
lemon_training = lemon_training.drop('Transmission',1)
lemon_training = lemon_training.drop('WheelTypeID',1)
lemon_training = lemon_training.drop('WheelType',1)
lemon_training = lemon_training.drop('Nationality',1)
lemon_training = lemon_training.drop('Size',1)
lemon_training = lemon_training.drop('AUCGUART',1)
lemon_training = lemon_training.drop('BYRNO',1)
lemon_training = lemon_training.drop('VNZIP1',1)
lemon_training = lemon_training.drop('VNST',1)
lemon_training = lemon_training.drop('WarrantyCost',1)

clf = tree.DecisionTreeClassifier()
clf.fit(lemon_training, isBad)

clf.score(lemon_training, isBad)
cross_validation.cross_val_score(clf, lemon_training, isBad)
