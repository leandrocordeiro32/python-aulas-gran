numeros = [10, 24, 33, 36, 42, 6, 666]
print(numeros[6])



carros = ['HB20', 'Kicks', 'Argus', 'Ka', 'Ferrari', 'Jaguar', 'Fusca', 'Omega', 'Uno', 'Brasília', 'LandRover']
print('Lista de Carros: ', carros)
print(len(carros))

carros.append('Kombi')
print('Adicionando (append) a Kombi na lista de Carros: ',carros)

carros.remove('Ka')
print('Removendo (remove) o Ka da lista de Carros: ', carros)

del carros[3]
print('Removendo o item 3 (del carros[3]) da Lista de Carros: ', carros)

carros = sorted(carros)
print('Mudando a ordem dos items da lista (sorted): ', carros)

print('Adicionando vários carros para exemplificar impressão de lista item a item com o laço de repetição for: ', carros)

for carro in carros:
    print(f'Carro: {carro}')

lista = [1, 2, 3]
lista.append(4)
print(f"Adiciona o 4 na lista [1, 2, 3]: {lista}")

lista1 = [5, 6]
lista += lista1
print(f"União das listas [1, 2, 3] com a [5, 6]: {lista}")

lista[1] = 4
print(f"Troca o segundo item da lista [1, 2, 3, 4, 5] por 4: {lista}")