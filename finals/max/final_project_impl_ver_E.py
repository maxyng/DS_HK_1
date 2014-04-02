import pandas as pd
from sklearn.tree import DecisionTreeClassifier



def split_phrase(dataset):
	dataset['str_split'] = ''
	for x in range(dataset.shape[0]):
		dataset['str_split'][x] = str(dataset.Phrase[x]).strip().split(' ')
	return dataset

#load data (tsv)
train_base = pd.read_csv('./sentimental_rotton_tomato/train.tsv',sep='\t')
test_base = pd.read_csv('./sentimental_rotton_tomato/test.tsv',sep='\t')

#extract 'Phrase' and 'Sentiment'
train_base = split_phrase(train_base)
test_base = split_phrase(test_base)


clf = DecisionTreeClassifier().fit(train_base['str_split'], train_base['Sentiment'])
