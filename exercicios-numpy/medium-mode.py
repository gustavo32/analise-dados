# ⚫1- Substitua todos os números ímpares em arr com -1 sem alterar arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Saída desejada: array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
# arr == array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# ⚫2- Converta uma matriz 1D para uma matriz 2D com 2 linhas:
# np.arange(10)
# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Saída desejada:
# array([[0, 1, 2, 3, 4],
# [5, 6, 7, 8, 9]])

# ⚫3- Empilhe matrizes verticalmente:
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# Saída desejada:
# array([[0, 1, 2, 3, 4],
# [5, 6, 7, 8, 9],
# [1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1]])

# ⚫4- Empilhe as matrizes horizontalmente:
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# Saída desejada:
# array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
# [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])

# ⚫5- Crie o seguinte padrão sem codificação, usando apenas funções numpy e a matriz de entrada abaixo ‘a’.
# a = np.array([1,2,3])
# Saída desejada: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

import numpy as np

arr = np.arange(0, 10)
arr2 = arr.copy()
arr2[arr2 % 2 != 0] = -1
print("1- ")
print(arr2)
print(arr, "\n")

print("2- ")
arr = np.arange(10)
arr = np.reshape(arr, (2, 5))
print(arr, "\n")

print("3- ")
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
a = np.concatenate((a, b))
print(a, "\n")

print("4- ")
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
a = np.concatenate((a, b), axis=1)
print(a, "\n")

print("5- ")
a = np.array([1, 2, 3])
a = np.concatenate((a.repeat(3), np.tile(a, 3)))
print(a)
