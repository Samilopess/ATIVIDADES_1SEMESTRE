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