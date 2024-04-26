# Dupla: Samara ramos e louyse 

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f'{self.modelo} está ligado'
    def desligar(self):
        return f'{self.modelo} está desligado'
    def acelerar(self):
        return f'{self.modelo} está acelerando'

if __name__ == '__main__':
    carro1 = Carro('mercedes', 'amg 63', 2019, 'carbono')
    carro2 = Carro('toyota', 'sw4', 2020, 'branca')
    carro3 = Carro('honda', 'civic si', 2010, 'vermelho')

    print(carro1.ligar())
    print(carro2.desligar())
    print(carro3.acelerar())
    
    #atividade 2
    class Animal:
        def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def som(self):
        return f'{self.nome}: au au auu'
    
    def som(self):
        return f'{self.nome}: miau miau'
    
    def info(self):
        return f'{self.info}: é um animal doméstico'
    
if __name__ == '__main__':
    animal1 = Animal('Atlas', 10, 'Cachorro')
    animal2 = Animal('Fiona', 2, 'gato')
    
    print(animal1.som())
    print(animal2.som())
    print(animal1.info())
    print(animal2.info())
    
    
    # att 3
    
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
    
    
    # att 4
    
    
    class Produto:
        def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
    
    def nome(self):
        return self.nome

    def preço(self):
        return self.preço

    def estoque(self):
        return self.estoque
    
if __name__ == '__main__':
    produto1 = Produto('camiseta', 50, 5)
    produto2 = Produto('bermuda', 30, 10)
    produto3 = Produto('boné', 15, 8)

    print(produto1.preço())
    print(produto2.estoque())
    print(produto3.nome())
    
    
    # att 5
    
    class Triangulo:
        def __init__(self, lados):
        self.lados = lados

    def perimetro(self):
        return f'o triangulo tem {self.lados}'    
    def calcular(self):
        return