from datetime import datetime

def formatarData(data = datetime.now(), formato = '%d/%m/%Y'):
    return datetime.strftime(data, formato)

def criarData(data, formato = '%Y-%m-%d'):
    return datetime.strptime(data, formato)

'''
def formatarData(data = datetime.now()):
    return datetime.strftime(data, '%d/%m/%Y')

def formatarData():
    data = datetime(2023, 2, 17)
    return datetime.strftime(data, '%d/%m/%Y')
    # return datetime.strftime(data, '%d')

data1 = datetime(2026, 1, 8)
data2 = '2021-07-12' # não é do tipo data. É tipo string
data3 = criarData('2023-12-12')

print(f'Testanto datetime: {data1}')
print(f'Testando data como str: {data2}')

print(f'Testanto formatarData() para que informe a data conforme minhas formatações: {formatarData()}')
print(f'Testando outras possibilidades de formatação por meio do atributo formato: {formatarData(formato= '%d')}')
# print(f'Testanto formatarData() para que informe a data conforme minhas formatações: {formatarData(data1)}')
# print(f'Testanto formatarData() para que informe o dia da data: {formatarData()}')

print(f'Testando criarData: {formatarData(data3)}')
'''
