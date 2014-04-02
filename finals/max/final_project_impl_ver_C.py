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

base = base[base.str_length > 0]

result = base['Sentiment']
base = base.drop(['PhraseId','SentenceId','Sentiment','str_length'],axis=1)


vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(base.Phrase)

model = naive_bayes.BernoulliNB().fit(X_train, list(result))
print cross_validation.cross_val_score(naive_bayes.BernoulliNB(), X_train.toarray(), result)
fpr, tpr, thresholds = metrics.roc_curve(result, model.predict(X_train.toarray()), pos_label=1)
print metrics.auc(fpr, tpr)

#testset = pd.read_csv('./sentimental_rotton_tomato/test.tsv',sep='\t')
#testset = testset.drop(['PhraseId','SentenceId'],axis=1)

#X_test = vectorizer.fit_transform(testset.Phrase)
#predictions = model.predict_proba(X_test)[:,1]
