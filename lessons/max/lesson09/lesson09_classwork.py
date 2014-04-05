from sklearn import datasets, metrics
from matplotlib import pyplot as plt

iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points : %d" % (iris.target != y_pred).sum())

# Finding the false positive and true positive rates where the positive label is 2.
fpr, tpr, thresholds = metrics.roc_curve(iris.target, y_pred, pos_label=2)
metrics.auc(fpr, tpr)
plt.plot(fpr, tpr)
plt.show()