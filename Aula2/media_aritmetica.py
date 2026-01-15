n1 = float(input('Informa a primeira nota: '))
n2 = float(input('Informa a segunda nota: '))
n3 = float(input('Informa a terceira nota: '))
n4 = float(input('Informa a quarta nota: '))

soma = n1 + n2 + n3 + n4
media = soma / 4
if media >= 7:
    print(f'A média das suas notas é {media:.1f}')
    print('Você obteve aprovação!')
elif media < 5:
    print(f'A média das suas notas é {media:.1f}')
    print('Você não obteve aprovação! Estude mais no próximo semestre letivo!')
else:
    print(f'A média das suas notas é {media:.1f}')
    print('Você está de recuperação! Estude mais para a prova substitutiva!')
