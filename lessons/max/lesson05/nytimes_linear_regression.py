import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean,log
from sklearn import linear_model

nytimes = pd.read_csv('../../../data/nytimes_cleaned.csv')
nytimes_male = nytimes[nytimes['Gender']==1]
nytimes_female = nytimes[nytimes['Gender']==0]

male_age = [[x] for x in nytimes_male['Age'].values]
male_ctr = nytimes_male['Ctr'].values

female_age = [[x] for x in nytimes_female['Age'].values]
female_ctr = nytimes_female['Ctr'].values

regr_nytimes_male = linear_model.LinearRegression()
regr_nytimes_male.fit(male_age, male_ctr)
regr_nytimes_male.score(male_age, male_ctr)

regr_nytimes_female = linear_model.LinearRegression()
regr_nytimes_female.fit(female_age, female_ctr)
regr_nytimes_female.score(female_age, female_ctr)

plt.scatter(male_age,male_ctr)
plt.scatter(female_age,female_ctr)

plt.plot(male_age, regr_nytimes_male.predict(male_age), color='blue', linewidth=3)
plt.plot(female_age, regr_nytimes_female.predict(female_age), color='red', linewidth=3)