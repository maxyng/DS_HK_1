import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

lemon_training = pd.read_csv('C:\datascience\data\class\lemonsClassificationData\lemon_training.csv')
isBad = lemon_training['IsBadBuy']
lemon_training.drop['RefId']
lemon_training.drop['IsBadBuy']

lemon_training_numeric = ["VehYear","VehicleAge","WheelTypeID","VehOdo","MMRAcquisitionAuctionAveragePrice","MMRAcquisitionAuctionCleanPrice","MMRAcquisitionRetailAveragePrice","MMRAcquisitonRetailCleanPrice","MMRCurrentAuctionAveragePrice","MMRCurrentAuctionCleanPrice","MMRCurrentRetailAveragePrice","MMRCurrentRetailCleanPrice","BYRNO","VNZIP1","VehBCost","IsOnlineSale","WarrantyCost"]

lemon_training_numeric = lemon_training_numeric.fillna(0)

result = feature_selection.univariate_selection.f_regression(lemon_training_numeric,isBad)