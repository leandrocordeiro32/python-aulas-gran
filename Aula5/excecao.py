print("Vamos fazer uma divisão entre número inteiros?")
print()
'''
try:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    
    resultado = n1 / n2
    
    print(f"O resultado da divisão entre {n1} por {n2} é igual a {resultado}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
'''

try:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    
    resultado = n1 / n2
    
    print(f"O resultado da divisão entre {n1} por {n2} é igual a {resultado}")

except ValueError:
    print("Digitar apenas números inteiros!")

except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

# Outras possibilidades:

else:
    print("O programa foi executado corretamente!")

finally:
    print("Fim")


