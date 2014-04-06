import pandas as pd
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

#load data (tsv)
base = pd.read_csv('./sentimental_rotton_tomato/train.tsv',sep='\t')

base['str_split'] = ''
base['str_length'] = 0
for x in range(base.shape[0]):
	base['str_split'][x] = str(base.Phrase[x]).strip().split(' ')
	base['str_length'][x] = len(base['str_split'][x])

#base = base[base.str_length > 0]

X_splitwords = []
Y_result = []
#for x in range(base.shape[0]):
for x in range(10):
	for words in base.str_split[x]:
		#print words + ' ' + str(result[x])
		X_splitwords.append(words)
		Y_result.append(base['Sentiment'][x])

result = base['Sentiment']
base = base.drop(['PhraseId','SentenceId','Sentiment','str_length'],axis=1)

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
X_train = vectorizer.fit_transform(X_splitwords)

model = naive_bayes.MultinomialNB().fit(X_train, list(Y_result))
#print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), X_train.toarray(), list(Y_result))
#fpr, tpr, thresholds = metrics.roc_curve(Y_result, model.predict(X_train.toarray()), pos_label=1)
#print metrics.auc(fpr, tpr)


testset = pd.read_csv('./sentimental_rotton_tomato/test.tsv',sep='\t')

testset['str_split'] = ''
testset['str_length'] = 0
for x in range(testset.shape[0]):
	testset['str_split'][x] = str(testset.Phrase[x]).strip().split(' ')
	testset['str_length'][x] = len(testset['str_split'][x])

X_test_splitwords = []
#for x in range(base.shape[0]):
for x in range(10):
	for words in testset.str_split[x]:
		#print words + ' ' + str(result[x])
		X_test_splitwords.append(words)


testset = testset.drop(['PhraseId','SentenceId'],axis=1)

X_test = vectorizer.fit_transform(X_test_splitwords)
predictions = model.predict_proba(X_test)[:,1]
