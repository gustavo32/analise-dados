# ⚫1- Calcule as contagens de valores únicos na linha.

# np.random.seed(100)
# arr = np.random.randint(1,11,size=(6, 10))
# print(arr)
# array(
# [[ 9, 9, 4, 8, 8, 1, 5, 3, 6, 3],
# [ 3, 3, 2, 1, 9, 5, 1, 10, 7, 3],
# [ 5, 2, 6, 4, 5, 5, 4, 8, 2, 2],
# [ 8, 8, 1, 3, 10, 10, 4, 3, 6, 9],
# [ 2, 1, 8, 7, 3, 1, 9, 3, 6, 2],
# [ 9, 2, 6, 5, 3, 9, 4, 6, 1, 10]])
# Saída desejada:
# [[1, 0, 2, 1, 1, 1, 0, 2, 2, 0],
# [2, 1, 3, 0, 1, 0, 1, 0, 1, 1],
# [0, 3, 0, 2, 3, 1, 0, 1, 0, 0],
# [1, 0, 2, 1, 0, 1, 0, 2, 1, 2],
# [2, 2, 2, 0, 0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 2, 0, 0, 2, 1]]

# A saída contém 10 colunas representando números de 1 a 10. Os valores são as contagens dos números nas respectivas linhas.
# Por exemplo, Cell (0,2) tem o valor 2, o que significa que o número 3 ocorre exatamente 2 vezes na primeira linha.
import numpy as np


def count_row_and_substitute(data):
    for i in range(10):
        data[i] = ((data[i] == data).sum()-1)
    return data


print("1- ")
np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))
print(arr, "\n")
arr = np.apply_along_axis(count_row_and_substitute, 1, arr)
print(arr, "\n")

# ⚫2- Encontre todos os picos em uma matriz 1D numpy ‘a’. Picos são pontos cercados por valores menores em ambos os lados.
# a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
# Saída desejada:
# array([2, 5])
# onde, 2 e 5 são as posições dos valores de pico 7 e 6.


def peaks(data):
    esq = data - np.roll(data, 1)
    dire = data - np.roll(data, -1)
    return np.argwhere(((esq > 0) & (dire > 0))).T[0]


print("2- ")
np.random.seed(100)
a = np.random.randint(0, 20, size=(1, 10))[0, :]
print(a)
print(peaks(a))

