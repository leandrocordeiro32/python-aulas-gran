
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return 'Não é possível dividir um número por zero!'
    else:
        return n1 / n2
    
def calcular (n1, n2, operador):
    match operador:
        case '+':
            return soma(n1, n2)
        case '-':
            return subtracao(n1, n2)
        case '*':
            return multiplicacao(n1, n2)
        case '/':
            return divisao(n1, n2)
        case other:
            return 'Operador não encontrado!'

n1 = float(input("Digite um número qualquer: "))
n2 = float(input("Digite outro número qualquer: "))
operador = input("Informe o sinal de operação matemática (+) (-) (*) (/): ")
resultado = calcular(n1, n2, operador)

if isinstance(resultado, (int, float)):
    print(f"{n1} {operador} {n2} = {resultado:.2f}")
else:
    print(resultado)