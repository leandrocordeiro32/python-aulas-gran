arquivo = open('pessoas.txt', 'w+')
# arquivo = open('pessoas.txt', 'a+')

arquivo.write(input('Escreva um nome próprio: '))
arquivo.write('\nAssassina\n')
arquivo.write('Vingativa\n')

arquivo.seek(0)          # volta o cursor para o início
conteudo = arquivo.read()
print(conteudo)

arquivo.close()

# Outra forma de escrever o código:

with open('pessoas.txt', 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)