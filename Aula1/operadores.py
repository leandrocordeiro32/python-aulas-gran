n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

# Operadores Aritméticos

soma = n1 + n2
print("O resultado da soma entre {} e {} é igual a".format(n1, n2) , soma)

subtracao = n1 - n2
print("O resultado da subtração entre {} e {} é igual a".format(n1, n2) , subtracao)

multiplicacao = n1 * n2
print("O resultado da multiplicação entre {} e {} é igual a".format(n1, n2) , multiplicacao)

divisao = n1 / n2
print("O resultado da divisão entre {} e {} é igual a".format(n1, n2) , divisao)

resto = n1 % n2
print("O resto da divisão entre {} e {} é igual a".format(n1, n2) , resto)

# Operadores Relacionais

igualdade = n1 == n2
print ("O número {} é igual a {}?".format(n1, n2) , igualdade)

diferenca = n1 != n2
print ("O número {} é diferente de {}?".format(n1, n2) , diferenca)

maior_que = n1 > n2
print ("O número {} é maior que {}?".format(n1, n2) , maior_que)

menor_que = n1 < n2
print ("O número {} é menor que {}?".format(n1, n2) , menor_que)

maior_igual_a = n1 >= n2
print ("O número {} é maior ou igual a {}?".format(n1, n2) , maior_igual_a)

menor_igual_a = n1 <= n2
print ("O número {} é menor ou igual a {}?".format(n1, n2) , menor_igual_a)

_and = (n1 > 69) and (n2 <= 24)
print("O número {} é maior que 69 e o número {} é menor ou igual a 24?".format(n1, n2) , _and)

_or = (n1 <= 69) or (n2 >= 24)
print("O número {} é menor ou igual a 69 ou o número {} é maior ou igual a 24?".format(n1, n2) , _or)

_not = not ((n1 <= 69) or (n2 >= 24))
print("Negação de: o número {} é menor ou igual a 69 ou o número {} é maior ou igual a 24?".format(n1, n2) , _not)