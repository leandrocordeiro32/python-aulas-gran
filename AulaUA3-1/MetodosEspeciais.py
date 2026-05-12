# Métodos Especiais ou Mágicos 

# __init__

class Imovel:

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites

    # __add__
    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    # __gt__
    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    # __lt__
    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    # __str__
    def __str__(self):
        return str(self.__dict__)

# __dict__

casarao = Imovel('Casarão', 3, 4)
print(casarao.__dict__)

mansao = Imovel('Mansão', 4, 5)
print(mansao.__dict__)

soma = casarao + mansao
print(f'Testando o método __add__: soma dos quartos e suítes = {soma}')
print(f'Testando o método __gt__: casarao > mansao? {casarao > mansao}')
print(f'Testando o método __gt__: casarao < mansao? {casarao < mansao}')
print(f'Testando o método __str__: {casarao}')
print(f'Testando o método __str__: {mansao}')