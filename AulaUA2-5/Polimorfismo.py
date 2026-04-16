# exemplo simples que reúne os três pilares: herança. encapsulamento e polimorfismo

class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca # encapsulamento
        self.__modelo = modelo # encapsulamento
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, valor):
        self.__marca = valor
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor
        
    def mover(self):
        print("O veículo está se movendo.")
        
class Carro(Veiculo): # herança
    def mover(self):
        print(f'O carro {self.marca} - {self.modelo} está andando na estrada.')
        
   
class Moto(Veiculo): # herança
    def mover(self):
        print(f'A moto {self.marca} - {self.modelo} está empinando a roda da frente.')
        
class Barco(Veiculo): # herança
    def mover(self):
        print(f'O barco {self.marca} - {self.modelo} está navegando no mar.')     
        
# Criação dos Objetos

carro = Carro("Fiat", "Argo")
moto = Moto("Honda", "CB 500")
barco = Barco("Yamaha", "242X")

#polimorfismo - Todas as classes têm o método mover(), mas cada uma implementa esse método de forma diferente

veiculos = [carro, moto, barco]

for veiculo in veiculos:
    veiculo.mover()
        
# Setters

carro.marca = "Ford"
carro.modelo = "Ka"

carro.mover()