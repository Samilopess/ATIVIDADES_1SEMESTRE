class ContaBancaria:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    
    def sacar(self):
        saque = int(input('Digite o seu saque: '))
        self.saldo -= saque
        return f'o seu saque foi de R${saque}'

    def depositar(self):
        deposito = int(input('Depositar o valor: '))
        deposito += self.saldo
        return deposito
    
    def saldo (self):
        return int(f'seu saldo atual é{self.saldo}.')  
if __name__ == '__main__':
    conta1 = ContaBancaria('123', 1000, 'Johnatas')
    print(f"O depósito foi de R${conta1.depositar()}")
    print(conta1.sacar())
    print(conta1.saldo())