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

class EventoOnline(Evento):
    def __init__(self, nome):
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local)


    def imprimi_informacoes(self):
        print(f'ID do evento: {self.id}')
        print(f'Nome do evento: {self.nome}')
        print(f'Link para acessar o evento: {self.local}')
        print('----------------------------------------------------')

ev_online = EventoOnline("Live de Python")
ev_online.imprimi_informacoes()

ev_online2 = EventoOnline("Live de JavaScript")
ev_online2.imprimi_informacoes()

ev = Evento("Aula de Python local", "Marigá-PR")
ev.imprimi_informacoes()
