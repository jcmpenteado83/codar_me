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

    #método de classe > atributo de classe >atributo que tem que ser compartilhado entre todos os objetos da mesma classe
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f"https://tamarcado.com/eventos?id={cls.id}")
        return evento

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

ev_online = Evento.cria_evento_online("Live de Python")
ev_online.imprimi_informacoes()

ev_online2 = Evento.cria_evento_online("Live de JavaScript")
ev_online2.imprimi_informacoes()

