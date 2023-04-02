from evento import Evento


class EventoOnline(Evento):
    def __init__(self, nome):
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        super().__init__(nome, local)

    def imprimi_informacoes(self):
        print(f'ID do evento: {self.id}')
        print(f'Nome do evento: {self.nome}')
        print(f'Link para acessar o evento: {self.local}')
        print('----------------------------------------------------')
