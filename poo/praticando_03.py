class Carro:
    def __init__(self, marca, ano): # Construtor
        self.marca = marca
        self.ano = ano
        self.velocidade = 0
        self.posicao = 0

    def acelerar(self, intensidade): # Método de instância
        if intensidade == 1:
            self.velocidade += 5
        elif intensidade == 2:
            self.velocidade += 10
            self.posicao = self.posicao + self.velocidade

    def imprime_estado(self): # Método de instância
        print("Dados do carro ", self.marca)
        print("O ano do carro é: ", self.ano)
        print("A posição do carro é: ", self.posicao)
        print("A velocidade do carro é: ", self.velocidade)

    @classmethod
    def cria_toyota_2021(cls): # Método de classe
        return cls(marca="Toyota", ano=2021)

    @staticmethod
    def calcula_posicao(pos_atual, velocidade): # Método estático
        return pos_atual + velocidade


carro_a = Carro("Volkswagen", 2019)
carro_b = Carro("Toyota", 2020)
carro_a.acelerar(2)
carro_b.acelerar(1)
carro_a.imprime_estado()
carro_b.imprime_estado()
