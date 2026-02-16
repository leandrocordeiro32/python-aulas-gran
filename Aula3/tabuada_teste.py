# Você está desenvolvendo um programa em Python para exibir uma tabela de multiplicação, em que cada número de 1 a 5 é multiplicado pelos números de 1 a 10. Para isso, você utiliza o conceito de for aninhado para percorrer os números de 1 a 5 e, para cada um deles, percorrer os números de 1 a 10. Considerando essas informações, qual das opções a seguir apresenta a implementação correta para exibir a tabela de multiplicação?

print("Alternativa 1")
for i in range(1, 6):

    for j in range(1, 11):

        resultado = i * j

        print(f"{i} x {j} = {resultado}")

print("Alternativa 2")
for i in range(1, 11):

    for j in range(1, 6):

        resultado = i * j

        print(f"{i} x {j} = {resultado}", end=" ") 
    print()

print("Alternativa 3")
for i in range(1, 11):

    for j in range(1, 6):

        resultado = j * i

        print(f"{j} x {i} = {resultado}", end=" ") 
        print()

print("Alternativa 4")
for i in range(1, 6):

    for j in range(1, 11):

        resultado = j * i

        print(f"{j} x {i} = {resultado}", end=" ") 
        print()

print("Alternativa 5")
for i in range(1, 6):

    for j in range(1, 11):

        resultado = i * j

        print(f"{i} x {j} = {resultado}", end=" ") 
        print()

print("ChatGPT")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()  # linha em branco entre tabuadas