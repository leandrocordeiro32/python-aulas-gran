print()
print("########### Votação com While ###########")
print()

candidato1 = 0
candidato2 = 0
votos_nulos = 0
votos_totais = 0

while True:
    voto = int(input("Digite o número do candidato (1 ou 2): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        votos_nulos += 1

    votos_totais += 1
    continuar = input("Deseja continuar votando? (s/n): ")
    if continuar == "n":
        break

print(f"Total de votos: {votos_totais}")
print(f"Candidato 1 recebeu {candidato1} votos")
print(f"Candidato 2 recebeu {candidato2} votos")
print(f"Votos nulos: {votos_nulos}")


