import requests

def get_cotacao(destino = 'BRL'):
    
    url = 'https://api.exchangerate-api.com/v4/latest/BRL' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        
        return data["rates"]

    else:
        print("Erro ao obter cotacao: ", response.status_code)
        return None

def converter_cotacao(origem = 'USD', destino = 'BRL', valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 4)

def menu():
    print()
    print('1 - Converter Dólar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra Cotação')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    destino = 'BRL'
    valor = float(input("Informe o valor a ser convertido: "))

    print()

    match opcao:
        case 1: origem = 'USD'
        case 2: origem = 'EUR'
        case 3: origem = 'GBP'
        case 4:
            origem = input('Digite a Origem: ')
            destino = input("Digite o Destino: ")
            print()


    if opcao:
        print(f'{origem} em {destino}: {converter_cotacao(origem, destino, valor)}')
