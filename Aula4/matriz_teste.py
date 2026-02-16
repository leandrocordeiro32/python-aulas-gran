matriz = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [1, 2, 3, 5],
    [1, 3, 7, 13],
]

print("Alternativa 1")
for linha in range(len(matriz)):

    for coluna in range(len(matriz[linha])):

        print(f"Elemento da linha {linha+1} e coluna {coluna+1}: ", matriz[linha][coluna])


'''
print("Alternativa 2")
for linha in matriz:

    for coluna in matriz:

        print(matriz[linha][coluna])
'''

print("Alternativa 3")	
for linha in matriz:

    for elemento in linha:

        print(elemento)

print("Alternativa 4")	
for coluna in range(len(matriz)):

    for linha in range(len(matriz[coluna])):

        print(matriz[linha][coluna])

print("Alternativa 5")	
for elemento in matriz:

    for linha in matriz:

        print(elemento)