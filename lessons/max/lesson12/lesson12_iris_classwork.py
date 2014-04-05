## Iris Data Application
from sklearn import datasets,metrics,cluster
iris = datasets.load_iris()
cls = cluster.k_means(iris.data, 3)

sil = metrics.silhouette_score(iris.data,cls[1])

plt.subplot(211)
plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=iris.target)
plt.subplot(212)
plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=list(cls[1]))
plt.show()

