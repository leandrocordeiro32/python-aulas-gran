from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area
        
    def detalhar(self):
        print(self.__dict__)
        
    def calcularImposto(self):
        return print(self.valor * 0.02)
    
    @abstractmethod
    def aluguelSugerido(self):
        ...
    
class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco, area)
        #Imovel.__init__(self, nome, uf, valor, endereco, area)
        self.quartos = 0
        self.piscina = True
        
    def aluguelSugerido(self):
        return self.valor * 0.01
    
class ImovelComercial(Imovel):
    
    def aluguelSugerido(self):
        return self.valor * 0.015
    
class ImovelRural():
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva
        
    def mesPlantacao(self, mes):
        match mes:
            case 1: print ('Milho')
            case 2: print ('Feijão')
            case 3: print ('Soja')
            case other: print ('Algodão')
            
class Fazenda(Imovel, ImovelRural):
    def aluguelSugerido(self):
        return self.valor * 0.025
    
# imovel = Imovel('Solar Power', 'DF', 500000)
# imovel.endereco = 'Rua do Inferno'
# imovel.area = '2000'

# imovel.detalhar()

casa = ImovelResidencial('Casa da Mãe Joana', 'SP', 1000000)
casa.detalhar()
print(casa.aluguelSugerido())


clinica = ImovelComercial('Clinica Eva & Adão', 'SP', 5000000)
clinica.detalhar()
print(clinica.aluguelSugerido())
    
fazenda = Fazenda('Fazenda do Maia', 'GO', 15000000)
fazenda.detalhar()
fazenda.mesPlantacao(2)
fazenda.calcularImposto()
