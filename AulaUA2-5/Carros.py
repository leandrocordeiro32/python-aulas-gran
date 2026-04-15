class Carro:
    
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    def definir_informacoes(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        
    def mostrar_informacoes(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Ano: {self.__ano}')
        
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
        
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano
        
carro1 = Carro("Toyota", "Corolla", 2022)

carro1.set_marca("Honda")
carro1.set_modelo("Civic")
carro1.set_ano(2024)

print('------------------------------------------')

print(carro1.get_marca())
print(carro1.get_modelo())
print(carro1.get_ano())

print('------------------------------------------')

carro1.mostrar_informacoes()

print('------------------------------------------')