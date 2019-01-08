# ⚫1- Calcule a pontuação softmax de ‘sepal length’:

# url = ‘https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data’
# sepallength = np.genfromtxt(url, delimiter=’,’, dtype=’float’, usecols=[0])

# ⚫2- Filtre as linhas de iris_2d que possuem petallength (coluna 3) > 1.5 e sepallength (coluna 1) < 5.0

# url = ‘https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data’
# iris_2d = np.genfromtxt(url, delimiter=’,’, dtype=’float’, usecols=[0,1,2,3])

# ⚫3- Selecione as linhas de iris_2d que não têm nenhum valor ‘nan’

# url = ‘https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data’
# iris_2d = np.genfromtxt(url, delimiter=’,’, dtype=’float’, usecols=[0,1,2,3])


import numpy as np


print("1- ")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
sepallength = np.genfromtxt(url, delimiter=",", dtype=float, usecols=[0])

theta = 1
ps = np.exp(theta*sepallength)
ps /= np.sum(ps)

# sepal length normalizado pela softmax
print(ps, "\n")

print("2- ")

iris2d = np.genfromtxt(url, delimiter=",", dtype=float, usecols=[0, 1, 2, 3])
mask = (iris2d[:, 2] > 1.5) & (iris2d[:, 0] < 5.0)
print(iris2d[mask], "\n")

print("3- ")

iris2d = np.genfromtxt(url, delimiter=",", dtype=float, usecols=[0, 1, 2, 3])
mask = np.isfinite(iris2d)
print(iris2d[mask].reshape(-1, 4))
