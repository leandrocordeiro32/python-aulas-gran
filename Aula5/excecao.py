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
    # Código que pode gerar uma exceção
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    
    resultado = n1 / n2
    
    print(f"O resultado da divisão entre {n1} por {n2} é igual a {resultado}")

except ValueError:
    # Código para tratar exceção de valor inválido
    print("Digitar apenas números inteiros!")

except ZeroDivisionError:
    # Código para tratar exceção de divisão por zero
    print("Não é possível dividir um número por zero!")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

# Outras possibilidades:

else:
    # Código que será executado se não houver exceções
    print("O programa foi executado corretamente!")

finally:
    # Código que será executado sempre, com ou sem exceções
    print("Programa encerrado")


