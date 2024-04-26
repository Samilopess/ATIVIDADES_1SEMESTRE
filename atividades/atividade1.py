  # Dupla: samara ramos e louyse beatriz

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
        