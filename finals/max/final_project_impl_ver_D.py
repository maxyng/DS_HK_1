import pandas as pd
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
	return dict([(word,True) for word in words])

def split_phrase(dataset):
	dataset['str_split'] = ''
	for x in range(dataset.shape[0]):
		dataset['str_split'][x] = str(dataset.Phrase[x]).strip().split(' ')
	return dataset

def classify_phrase(phrase):
	return classifier.classify(word_feats(phrase))

#load data (tsv)
train_base = pd.read_csv('../../data/max/sentiment/train.tsv',sep='\t')
test_base = pd.read_csv('../../data/max/sentiment/test.tsv',sep='\t')

#extract 'Phrase' and 'Sentiment'
train_base = split_phrase(train_base)
test_base = split_phrase(test_base)

trainfeats = [(word_feats(train_base['str_split'][f]),train_base['Sentiment'][f]) for f in range(train_base.shape[0])]

#build and train model
classifier = NaiveBayesClassifier.train(trainfeats)
classifier.show_most_informative_features()

#for f in range(100):
#for f in range(test_base.shape[0]):
#	print test_base['str_split'][f] , ' ' , classify_phrase(test_base['str_split'][f])

testfeats = [(word_feats(test_base['str_split'][f])) for f in range(test_base.shape[0])]
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)