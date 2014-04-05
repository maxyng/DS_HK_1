import pandas as pd
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

#load data (tsv)
base = pd.read_csv('../../data/max/sentiment/train.tsv',sep='\t')

# One-liner which applied len() call to each Phrase
base['str_length'] = base.Phrase.apply(lambda p: len(p))

base = base[base.str_length > 0]

result = base['Sentiment']

base = base.drop(['PhraseId','SentenceId','Sentiment','str_length'],axis=1)

# Try the TfidfVectorizer instead
# http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(base.Phrase)

model = naive_bayes.MultinomialNB().fit(X_train, list(result))

print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), X_train, result)

# Your scores are off because this implementation is restricted to the binary classification task.
fpr, tpr, thresholds = metrics.roc_curve(result, model.predict(X_train), pos_label=1)
print metrics.auc(fpr, tpr)

testset = pd.read_csv('../../data/max/sentiment/test.tsv',sep='\t')
testset = testset.drop(['PhraseId','SentenceId'],axis=1)

X_test = vectorizer.fit_transform(testset.Phrase)
# predictions = model.predict_proba(X_test)[:,1]
