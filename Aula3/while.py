
print('-*-' * 15)
print("+++++++++++++++++++++++++++")
print("+++++++++ TABUADA +++++++++")
print("+++++++++++++++++++++++++++")
print()

continuar = True

while continuar:

    numero_tab = int(input("A Tabuada de qual número V.Majestade deseja? "))

    for i in range(1, 11):
        print(f"{numero_tab} x {i} = {numero_tab * i}")

    continuar = input('Deseja saber a tabuada de outro número? (s/n): ')
    continuar = True if continuar == 's' else False

print()
print("+++++++++++++++++++++++++++")
print("++++++++++ MÉDIA ++++++++++")
print("+++++++++++++++++++++++++++")
print()

soma = 0
contador = 0
qtd_numeros = int(input("Digite a quantidade de números a serem informados: "))

while contador < qtd_numeros:
    numero_med = int(input("Digite um número inteiro: "))
    soma += numero_med
    contador += 1

media = soma / qtd_numeros
print(f"A média dos números é igual a: {media}")

print('-*-' * 15)
