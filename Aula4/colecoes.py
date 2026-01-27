# Conjuntos

conjunto = set([4, 5, 9, 14, 23])
print('Conjunto: ', conjunto)

#Tupla

tupla = (3, 2, 4, 6, 0)
print('Tupla: ', tupla)

#Dicionário

pessoa = {'nome': 'Leona', 'telefone': '(61) 98524-6924', 'e-mail':'leona@vingativa.com'}
print('Nome: ', pessoa['nome'])
print('Telefone: ', pessoa['telefone'])
print('E-mail: ', pessoa['e-mail'])

pessoas = [
    {'nome': 'Leona', 'telefone': '(61) 98524-6924', 'e-mail':'leona@vingativa.com'},
    {'nome': 'Mirela', 'telefone': '(61) 99924-6666', 'e-mail':'mirela@correaqui.com'},
    {'nome': 'Patixa', 'telefone': '(61) 98694-2424', 'e-mail':'patixa@manaus.com'}
]

print('Pessoa 0:', pessoas[0]['telefone'])
print('Pessoa 1:', pessoas[1]['nome'])