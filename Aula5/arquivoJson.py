import json

pessoas = [
    {'nome': 'Leona', 'telefone': '(61) 98524-6924', 'e-mail':'leona@vingativa.com'},
    {'nome': 'Mirela', 'telefone': '(61) 99924-6666', 'e-mail':'mirela@correaqui.com'},
    {'nome': 'Patixa', 'telefone': '(61) 98694-2424', 'e-mail':'patixa@manaus.com'}
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)