
print()
print("Tabuada de 2")
print()

for i in range(1, 11):
    # print("2 x {} = {}".format(i, 2*i))
    # print("2 x", i, " =", 2*i)
    print(f"2 x {i} = {2*i}")

print()
print("Votação")
print()

candidato_1 = 0
candidato_2 = 0
votos_nulos = 0

for i in range(30):
    voto = int(input(f"Digite o voto da pessoa estudante {i+1}: "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    else:
        votos_nulos += 1

print(f"Total de votos para a pessoa candidata 1: {candidato_1}")
print(f"Total de votos para a pessoa candidata 2: {candidato_2}")
print(f"Total de votos nulos: {votos_nulos}")

print()
print("Média de números inteiros")
print()

soma = 0
numeros = int(input("Informe a quantidade de números a serem informados: "))

for i in range(numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / numeros
print(f"A média dos números é: {media}")

