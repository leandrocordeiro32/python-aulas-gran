# Encapsulamento é um conceito da programação orientada a objetos que consiste em restringir o acesso direto aos dados de um objeto e permitir que eles sejam manipulados apenas por meio de métodos definidos na própria classe. Na prática, isso serve para proteger os dados e garantir que eles sejam usados de forma controlada.
# Python não tem encapsulamento “rígido” como outras linguagens, mas usa convenções de nomenclatura:

# Atributo Público: Pode ser acessado livremente.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome # público
        
p = Pessoa("Ana")
print(f'O nome da pessoa é {p.nome}.') # acesso direto

# Atributo protegido (_): Indica que não deveria ser acessado fora da classe (mas ainda é possível).

class Pessoa:
    def __init__(self, nome):
        self._nome = nome # protegido
        
class Estudante(Pessoa):
    def mostrar_nome(self):
        return self._nome # acesso funciona normalmente
    
e = Estudante("Leona")
print(f'O nome de estudante é {e.mostrar_nome()}.')

# Atributo privado (__): Dificulta o acesso direto (name mangling).

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome # privado
        
    def get_nome(self):
        return self.__nome
    
class Estudante(Pessoa):
    def mostrar_nome(self):
        return self.get_nome()
    
e = Estudante("Inês Brasil")
print(f'O nome de estudante é {e.mostrar_nome()}')

