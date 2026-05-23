
import pandas as pd

cidades = [
    {'nome': 'Distrito Federal' , 'uf': 'DF' , 'populacao': 1000000},
    {'nome': 'São Paulo' , 'uf': 'SP' , 'populacao': 31000000},
    {'nome': 'Rio de Janeiro' , 'uf': 'RJ' , 'populacao': 5000000},
    {'nome': 'Recife' , 'uf': 'PE' , 'populacao': 1100000},    
]

dataFrame = pd.DataFrame(cidades)
print(dataFrame)

ordenada = dataFrame.sort_values(by='populacao', ascending=False)
print(ordenada)
print()
print(ordenada.head(2)['nome'])