import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm,tree, cross_validation

lemon_training = pd.read_csv('C:\datascience\data\class\lemonsClassificationData\lemon_training.csv')
lemon_training =lemon_training.fillna(0)

isBad = lemon_training['IsBadBuy']
lemon_training = lemon_training.drop(['RefId','IsBadBuy','PurchDate','Auction','Make','Model','Trim','SubModel','Color','Transmission','WheelTypeID','WheelType','Nationality','TopThreeAmericanName','PRIMEUNIT','Size','AUCGUART','BYRNO','VNZIP1','VNST','WarrantyCost'],1)


clf =  svm.SVC()
clf.fit(lemon_training, isBad)

clf.score(lemon_training, isBad)
cross_validation.cross_val_score(clf, lemon_training, isBad)
