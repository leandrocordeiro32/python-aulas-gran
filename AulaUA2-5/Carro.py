# Melhores práticas

class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        
    # get_marca
    @property
    def marca(self):
        return self.__marca
    
    # set_marca
    @marca.setter
    def marca(self, valor):
        if valor:
            self.__marca = valor
            
    # get_modelo
    @property
    def modelo(self):
        return self.__modelo
    
    # set_modelo
    @modelo.setter
    def modelo(self, valor):
        if valor:
            self.__modelo = valor
            
    # get_ano
    @property
    def ano(self):
        return self.__ano
    
    # set_ano
    @ano.setter
    def ano(self, valor):
        if valor > 1886: # primeiro carrro da historia
            self.__ano = valor
        else:
            raise ValueError("Ano Inválido")
            
    def mostrar_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        
carro1 = Carro("Ford", "Ka", 2007)

print('------------------------------------------')
carro1.mostrar_informacoes()
print('------------------------------------------')

carro1.marca = "Honda"
carro1.modelo = "Civic"
carro1.ano = 2020

print('------------------------------------------')
carro1.mostrar_informacoes()
print('------------------------------------------')
