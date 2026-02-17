

def dividir(n1, n2):
    if n2 == 0:
        print("Não é possível dividir um número por 0")
    else:
        resultado = n1/n2
        # print(f"{n1} / {n2} = {resultado}")
        return resultado

divisao = dividir(10, 0)
print(f"{10} / {0} = {divisao}")

print("O resultado da divisão é", dividir(30, 0))

resultado = dividir(48, 2)
soma = 20 + resultado
print("O resultado da soma é", soma)

dividir(128, 2)