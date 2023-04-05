class Evento:
    id = 1

    #Construtores
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    #método instância
    def imprimi_informacoes(self):
        print(f'ID do evento: {self.id}')
        print(f'Nome do evento: {self.nome}')
        print(f'Local do evento: {self.local}')
        print('----------------------------------------------------')

    #método estático
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if area >= 5 and area < 10:
            return 5
        elif area >= 10 and area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0

