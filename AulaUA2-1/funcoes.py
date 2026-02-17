
def imprime_mensagem():
    print("Vamos aprender um pouco sobre função?")

imprime_mensagem()

def imprime_lista(lista):
    for elemento in lista:
        print(elemento)

minha_lista = ['ovos', 'banana', 'leite', 'tomate']
print("Elementos da minha lista:")
imprime_lista(minha_lista)

def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado
numero = float(input("Informe um número qualquer: "))
resultado = calcular_quadrado(numero)
print(f"O quadrado de {numero} é igual a {resultado}")

def maior_valor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior
lista_numeros = [1, 9, 40, 97, 666, 1001, 59999, 9999999990]
valor_maior = maior_valor(lista_numeros)
print(f"O maior valor da lista é {valor_maior}")

def dividir(n1, n2):
    if n2 == 0:
        print("Não é possível dividir um número por 0")
    else:
        resultado = n1/n2
        # print(f"{n1} / {n2} = {resultado}")
        return resultado

divisao = dividir(10, 0)
print(f"{10} / {0} = {divisao}")

print("O resultado da divisão é", dividir(30, 5))

resultado = dividir(48, 2)
soma = 20 + resultado
print("O resultado da soma é", soma)