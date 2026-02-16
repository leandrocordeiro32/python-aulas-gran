matriz = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [1, 2, 3, 5],
    [1, 3, 7, 13],
]

print('Imprime todos os itens da Matriz: ', matriz)
print('Imprime os itens da linha 2 da Matriz: ', matriz[2])
print('Imprime o item 3 da linha 0: ', matriz[0][3] )

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento da linha {i+1} e coluna {j+1}: ", matriz[i][j])