class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial # atributo privado
        
    # método para consultar saldo
    @property
    def saldo(self):
        return self.__saldo

    # método para depósito
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R$ {valor} realizado.')
        else:
            print("Valor inválido")

    # método para saque
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R$ {valor} realizado.')
        else:
            print("Saldo insuficiente ou valor inválido.")
        
# Usando a classe

conta = ContaBancaria("Leona", 100000000000)

print(f'Seu saldo atual é R$ {conta.saldo}')

conta.depositar(5000000)
print(f'Seu saldo atual é R$ {conta.saldo}')

conta.sacar(10000000000)
print(f'Seu saldo atual é R$ {conta.saldo}')
