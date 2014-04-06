import pandas as pd
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#load data (tsv)
base = pd.read_csv('./sentimental_rotton_tomato/train.tsv',sep='\t')

base['str_length'] = 0
for x in range(base.shape[0]):
	base['str_length'][x] = len(str(base.Phrase[x]).strip().split(' '))

base = base[base.str_length > 0]

result = base['Sentiment']
base = base.drop(['PhraseId','SentenceId','Sentiment','str_length'],axis=1)

# So let's introduce the TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
X_train = vectorizer.fit_transform(base.Phrase)

# Gausian Model doesn't handle sparse data well, in fact it crashed my python!
model = naive_bayes.MultinomialNB()
model.fit(X_train, result.values)
print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), X_train, result.values)
fpr, tpr, thresholds = metrics.roc_curve(result, model.predict(X_train), pos_label=1)
print metrics.auc(fpr, tpr)

#testset = pd.read_csv('./sentimental_rotton_tomato/test.tsv',sep='\t')
#testset = testset.drop(['PhraseId','SentenceId'],axis=1)

# X_test = vectorizer.fit_transform(testset.Phrase)
# predictions = model.predict_proba(X_test)[:,1]
