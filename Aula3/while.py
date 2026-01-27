continuar = True

while continuar:

    numero = int(input("A Tabuada de qual número V.Majestade deseja? "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    continuar = input('Deseja saber a tabuada de outro número? (s/n)')
    continuar = True if continuar == 's' else False