import csv

carros = [
    ['VW', 'Virtus', '2017'],
    ['VW', 'Gol', '1999'],
    ['Fiat', 'Argus', '2002'],
    ['Fiat', 'Toro', '2022']
]

with open('carros.csv', 'w', newline='') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=";")

    fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
    fileCSV.writerows(carros)