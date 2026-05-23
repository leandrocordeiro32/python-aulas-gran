import numpy as np

''' Média manual '''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 90, 100]

soma = 0

for n in numeros:
    soma += n

media = soma / len(numeros)

print (f'A media manual é igual a {media}')

''' Média Numpy '''
array_numeros = np.array(numeros)

medianp = np.mean(array_numeros)
print (f'A media usando numpy é igual a {medianp}')
