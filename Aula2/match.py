# Instrução match

sigla = str(input('Informe a sigla de um estado da região SUDOESTE do Brasil: '))

match sigla:
    case 'RJ':
        print('Rio de Janeiro')
    case 'SP':
        print('São Paulo')
    case 'MG':
        print('Minas Gerais')
    case 'ES':
        print('Espírito Santo')
    case other: # ou case _:
        print("A sigla não foi identificada como parte da região SUDOESTE do Brasil!")
    
    