# ⚫1- Importe numpy como ‘np’ e imprima o número da versão.

# ⚫2- Crie uma matriz 1D com números de 0 a 9
# Saída desejada:
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# ⚫3- Crie uma matriz booleana numpy 3×3 com ‘True’
# Saída desejada:
# array([[ True, True, True],
# [ True, True, True],
# [ True, True, True]], dtype=bool)

# ⚫4- Extraia todos os números ímpares de ‘arr’
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Saída desejada: array([1, 3, 5, 7, 9])

# ⚫5- Substitua todos os números ímpares arr por -1
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Saída desejada: array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])

import numpy as np

print("2- ")
array = np.arange(0, 10)
print(array, "\n")
print("3- ")
matriz = np.full((3, 3), True)
print(matriz, "\n")
print("4- ")
odd = array[(array % 2 != 0)]
print(odd, "\n")
print("5- ")
array[(array % 2 != 0)] = -1
print(array, "\n")
