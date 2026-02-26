'''
class Produto:
    pass

produto0 = Produto()
produto0.nome = 'Smartphone'
produto0.marca = 'Iphone'

produto1 = Produto()
produto1.nome = 'Geladeira'
produto1.marca = 'Electrolux'

print (produto0.__dict__)
print (produto1.__dict__)

class Produto:
    
    def __init__(self):
        self.nome = ''
        self.marca = ''
        self.modelo = 'LG'
        self.valor = 0
        
produto0 = Produto()
produto0.marca = 'Samsung'
produto0.valor = 5000

produto1 = Produto()

print (produto0.__dict__)
print (produto1.__dict__)
'''

class Produto:
    
    def __init__(self, nome, valor, quantidade = 0, marca = '', modelo = ''):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.marca = marca
        self.modelo = modelo
        
    def vender(self, quantidade):
        if (quantidade > self.quantidade):
            print("Não há produtos suficientes para esta venda. Estoque disponível: ", self.quantidade)
        else:
            self.quantidade -= quantidade
        
    def comprar(self, quantidade):
        self.quantidade += quantidade
        
produto0 = Produto('Smartphone', 14000, 100, 'Iphone', '20')
produto0.comprar(10)

produto1 = Produto('Geladeira', 3000, 10, 'Brastemp', 'BST900')
produto1.vender(9)

produto2 = Produto('TV', 2000)
produto2.vender(100)

print (produto0.__dict__)
print (produto1.__dict__)
print (produto2.__dict__)

