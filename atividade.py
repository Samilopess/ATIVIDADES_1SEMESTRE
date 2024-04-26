class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def freiar(self):
        return self.freiar
    def acelerar(self):
        return self.acelerar
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    def abrir_porta(self):
        return self.abrir_porta
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def empinar(self):
        return self.empinar
    
if __name__ == '__main__':
    carro1 = Carro("bmw", "x6", "branca")
    moto1 = Moto("Yamara", "XJ6", "600")
    print(F'Marca: {carro1.marca}\n Modelo: {carro1.modelo}\n Cor: {carro1.cor}')
    print(F'Marca: {moto1.marca}\n Modelo: {moto1.modelo}\n Cilindrda: {moto1.cilindrada}')