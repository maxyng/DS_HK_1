import pandas as pd
import nltk.classify.util
from nltk import DecisionTreeClassifier


def word_feats(words):
	return dict([(word,True) for word in words])

def split_phrase(dataset):
	dataset['str_split'] = ''
	for x in range(dataset.shape[0]):
		dataset['str_split'][x] = str(dataset.Phrase[x]).strip().split(' ')
	return dataset

#load data (tsv)
train_base = pd.read_csv('../../data/max/sentiment/train.tsv',sep='\t')
test_base = pd.read_csv('../../data/max/sentiment/test.tsv',sep='\t')


#extract 'Phrase' and 'Sentiment'
train_base = split_phrase(train_base)
test_base = split_phrase(test_base)

trainfeats = [(word_feats(train_base['str_split'][f]),train_base['Sentiment'][f]) for f in range(train_base.shape[0])]

testfeats = [(word_feats(test_base['str_split'][f])) for f in range(test_base.shape[0])]

classifier = nltk.DecisionTreeClassifier.train(trainfeats)
nltk.classify.accuracy(classifier, testfeats)

#clf = DecisionTreeClassifier().fit(list(train_base['Phrase']), train_base['Sentiment'])
