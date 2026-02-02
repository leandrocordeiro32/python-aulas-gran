# Inicializa a lista de produtos vazia
produtos = []

# Verifica se existe um arquivo de produtos e o carrega
try:
    with open('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            codigo, nome, quantidade = linha.strip().split(',')
            produtos.append({'codigo': codigo, 'nome': nome, 'quantidade': int(quantidade)})

except FileNotFoundError:
    pass

while True:
    # Exibe o menu de opções
    print('\n\nEscolha uma opção:')
    print('1 - Incluir produto')
    print('2 - Consultar produto')
    print('3 - Alterar produto')
    print('4 - Excluir produto')
    print('5 - Listar produtos')
    print('0 - Sair')

    opcao = input('Digite a opção desejada: ')