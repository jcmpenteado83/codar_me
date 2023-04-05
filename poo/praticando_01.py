class Carro:
    def __init__(self, marca, modelo, ano, cor, estado):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.estado = estado

    def ligar(self):
        print("Ligando o carro...")

    def desligar(self):
        print("Desligando o carro...")

    def dados(self):
        dado = dict()
        dado["Marca"] = self.marca
        dado["Modelo"] = self.modelo
        dado["Ano"] = self.ano
        dado["Cor"] = self.cor
        dado["Estado"] = self.estado
        dado = [dado]
        print(dado)


carro1 = Carro('Peugeot', '308', '2016', 'Preto', 'Usado')
carro1.dados()

carro2 = Carro('Fiat', 'Argo', '2021', 'Branco', 'Usado')
carro2.dados()

carro3 = Carro('VolksWagem', 'Polo', '2023', 'Prata', 'Novo')
carro3.dados()
