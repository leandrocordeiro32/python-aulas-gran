

soma = 0
numeros = int(input("Informe a quantidade de números a serem informados: "))

for i in range(numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / numeros
print(f"A média dos números é: {media}")

