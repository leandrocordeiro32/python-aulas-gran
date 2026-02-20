numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#def impar(n):
#    return n % 2 == 1

resultado = filter(lambda n: n % 2 == 1, numeros)
print(list(resultado))

palavras = ['bala', 'desejo', 'beijo', 'cultura', 'livre']
b_words = list(filter(lambda s: s.startswith('b'), palavras))
print("Palavras com a letra B: ", b_words)

frase = input("Digite uma frase: ")
if frase.startswith("A vida"):
    print("A string começa com 'A vida'!")
else:
    print(f"A string não começa com 'A vida'!")