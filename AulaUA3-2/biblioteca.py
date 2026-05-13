import math
import random

print(f'Apresentando o valor de PI com o método math.pi: {math.pi}')
print(f'Arredondando o valor de PI para baixo usando o método math.floor(): {math.floor(math.pi)}')
print(f'Arredondando o valor de PI para cima usando o método math.ceil(): {math.ceil(math.pi)}')

nota = float(input("Digite um número decimal com mais de 3 casas após a vírgula: "))
print(f'Arredondando a nota com o método round {nota}: {round(nota, 2)}')
print(f'Arredondando para baixo usando o método math.floor(): {math.floor(nota)}')
print(f'Arredondando para cima usando o método math.ceil(): {math.ceil(nota)}')

print(f'Gerando números aleatórios utilizando o método random.random() x 100 combinado com o round para arredondar: {round(random.random() * 100)}')

print(f'Gerando número inteiro aleatório, dentro de um intervalo, com random.randint(x, y): {random.randint(1, 99)}')

