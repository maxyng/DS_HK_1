## Iris Data Application
from sklearn import datasets,metrics,cluster
from matplotlib import pyplot as plt
iris = datasets.load_iris()

pca = PCA()
pca.fit(iris.data)

plt.plt(range(4),pca.explained_variance_)
plt.show()



from sklearn.decomposition import PCA, KernelPCA

kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=6)
X_kpca = kpca.fit_transform(iris.data)
X_back = kpca.inverse_transform(X_kpca)
pca = PCA()
X_pca = pca.fit_transform(iris.data)