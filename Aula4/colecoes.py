# Conjuntos (set) é uma coleção não ordenada de elementos únicos e imutáveis. Em outras palavras, um conjunto não permite elementos duplicados, e não é possível alterar um elemento individualmente após sua inclusão no conjunto.
print()
print("CONJUNTOS")
print()

conjunto = set([4, 4, 5, 9, 9, 14, 23])
print('Conjunto A: ', conjunto)
print("* O elemento 5 pertence ao Conjunto A? ", 5 in conjunto)

conjunto.add(24)
print("* Adiciona o número 24 ao Conjunto A: ", conjunto)

conjunto.remove(14)
print("* Remove o número 14 do Conjunto A: ", conjunto)

print()

conjunto1 = set([1, 2, 3, 4])
conjunto2 = set([3, 4, 5, 6])
print("Conjunto 1 = ", conjunto1)
print("Conjunto 2 = ", conjunto2)

# uniao = conjunto1 | conjunto2
uniao = conjunto1.union(conjunto2)
print(f"* A união dos conjuntos 1 = {conjunto1} e 2 = {conjunto2} é U = {uniao} ")

print()

# intersecao = conjunto1 & conjunto2
intersecao = conjunto1.intersection(conjunto2)
print(f"* A interseção dos conjuntos 1 = {conjunto1} e 2 = {conjunto2} é ∩ = {intersecao} ")

print()

# diferenca = conjunto1 - conjunto2
diferenca = conjunto1.difference(conjunto2)
print(f"* A diferença dos conjuntos 1 = {conjunto1} e 2 = {conjunto2} é 1 - 2 = {diferenca} ")

print()

print("TUPLA")
print()

#Tupla

tupla = (3, 2, 4, 6, 0)
print('Tupla: ', tupla)
print("* Elemento na posição 2 da tupla: ", tupla[1])
print("* Elementos entre 3 e 0 da tupla: ", tupla[1:4])

a, b, c, d, e = tupla
print("* Atribuindo valores aos elementos da tupla:")
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
print("e = ", e)

print("* Utilizando o loop for para percorrer cada elemento da tupla:")
for elemento in tupla:
    print(elemento)

print()

#Dicionário

pessoa = {'nome': 'Leona', 'telefone': '(61) 98524-6924', 'e-mail':'leona@vingativa.com'}
print('Nome: ', pessoa['nome'])
print('Telefone: ', pessoa['telefone'])
print('E-mail: ', pessoa['e-mail'])

pessoa['idade'] = 24

print('* Dicionário adicionando a Idade: ', pessoa)

pessoa['idade'] = 18
print('* Idade alterada para', pessoa['idade'], 'anos')

valor_removido = pessoa.pop('e-mail')
print("* Dicionário após remoção do campo 'e-mail: ", pessoa)
print("* Valor removido: ", valor_removido)

print()

pessoas = [
    {'nome': 'Leona', 'telefone': '(61) 98524-6924', 'e-mail':'leona@vingativa.com'},
    {'nome': 'Mirela', 'telefone': '(61) 99924-6666', 'e-mail':'mirela@correaqui.com'},
    {'nome': 'Patixa', 'telefone': '(61) 98694-2424', 'e-mail':'patixa@manaus.com'}
]

print("Lista + Dicionário: ", pessoas)
print('Pessoa 0 da lista:', pessoas[0]['telefone'])
print('Pessoa 1 da lista:', pessoas[1]['nome'])

print()
print("Percorrendo chaves, valores ou os dois na Lista do Dicionário com loop for:")
print()

for chave in pessoas:
    print("* Chave:", chave)

for valor in pessoas:
    print("Valor: ", list(valor.values()))

for pessoa in pessoas:
    for chave, valor in pessoa.items():
        print(chave, "=", valor)