#!/usr/bin/env python

import pandas as pd
from numpy import mean
#initialize dataframe

def divZeroFix(x):
	if x == 0:
		return 1
	else:
		return x

def map_gender(x):
	if x == 1:
		return 'Male'
	elif x == 0:
		return 'Female'
	else:
		return 'Alien'

final_df = pd.DataFrame()

"""
Loop through numbers 1 to 30 to gather nyt1.csv to nyt30.csv
append to final_df DataFrame
"""
for i in range(1,31):
#for i in range(1,5):
	df = pd.read_csv('./nyt/nyt'+str(i)+'.csv')
	final_df = final_df.append(df)

#Change 1 to Male, 0 to Female mapping in dataframe
final_df['Gender'] = final_df['Gender'].apply(map_gender)
#calculate clicks/impressions from dataframe
final_df['ctr'] = (final_df['Clicks'].astype(float)/(final_df['Impressions']).apply(divZeroFix))
final_df['1'] = 1

#perform some stats
df_mean = final_df[ ['Age', 'Gender', 'ctr'] ].groupby(['Age','Gender']).agg([mean])
df_count = final_df[['Age','Gender']].groupby(['Age','Gender'])
#print dfg.describe()

print final_df[:10]
print df_mean[:10]
print df_count.size()

#print results
#final_df.to_csv('nytimes_aggregation.csv')
#df_mean.to_csv('nytimes_mean_stat.csv')
df_count.size().to_csv('nytimes_count_stat.csv')