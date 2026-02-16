print("-*-" * 27)
print("-*-" * 10, "* MEDIA DAS NOTAS *", "-*-" * 10)
print("-*-" * 27)
print()

notas = []
soma = 0

for i in range(4):
    n = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(n)

for nota in notas:
    soma += nota

media = soma /len(notas)
print(f"A média das notas é: {media}")