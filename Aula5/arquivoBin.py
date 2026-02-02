arquivo = open('filename.bin', 'rb')

# Lendo dados do arquivo binário
data = arquivo.read()

# Gravando dados no arquivo binário
arquivo.write(data)

arquivo.close()