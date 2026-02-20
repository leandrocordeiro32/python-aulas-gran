numeros = [5, 6, 24, 69]

resultado = []

for n in numeros:
    resultado.append(n*2)
    
print("Utilizando loop for: ", numeros, resultado)

# Utilizando função: 
def multiplicar (n1):
    return n1 * 2

resultado = map(multiplicar, numeros)
print("Utilizando função: ", numeros, list(resultado))

# Utilizando lambda, ideal quando não houver reutilização de código:
resultado1 = map(lambda n: n * 2, numeros)
print("Utilizando lambda: ",numeros, list(resultado1))