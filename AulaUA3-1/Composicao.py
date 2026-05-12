# Composição

class Categoria:

    def __init__(self, tipo = ''):
        self.tipo = tipo
        
    def taxaAgua(self, consumo):
        match self.tipo:
            case 'Clínica': return consumo * 1
            case 'Restaurante': return consumo * 2
            case 'Hotel': return consumo * 2.5

class Imovel:

    imposto = 0.2

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()

    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther

    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther

    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def __str__(self):
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print('Chamou o método estático sem criar objeto.')

    @classmethod
    def metodoClasse(cls):
        print('Chamou o método de classe que vê o imposto.', cls.imposto)


casarao = Imovel('Casarão', 3, 4)
mansao = Imovel('Mansão', 4, 5)

categoria = Categoria('Hotel')
hotel = Imovel('Hotel Prazeres', 0, 150)
hotel.categoria = categoria
print(f'Testando Composição. A taxa de água é R$ {hotel.categoria.taxaAgua(300)}.')


'''
Imovel.metodoEstatico()

Imovel.metodoClasse()

print(f'Testando método somarAposentos: soma dos aposentos do casarão = {casarao.somarAposentos()}')
print(f'Testando método somarAposentos: soma dos aposentos da mansão = {mansao.somarAposentos()}')


soma = casarao + mansao
print(f'Testando o método __add__: soma dos quartos e suítes = {soma}')
print(f'Testando o método __gt__: casarao > mansao? {casarao > mansao}')
print(f'Testando o método __gt__: casarao < mansao? {casarao < mansao}')
print(f'Testando o método __str__: {casarao}')
print(f'Testando o método __str__: {mansao}')
'''