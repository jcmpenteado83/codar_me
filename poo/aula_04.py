# construtores
class Evento:
    def __init__(self, nome):
        self.nome = nome

    def altera_nome_evento(self, novo_nome):
        print("Alterando o nome do evento")
        self.nome = novo_nome

#variável + Classe = Cria um Objeto do tipo Evento com um evento/simbolo apontando para ele
ev = Evento("Aula de python")
ev2 = Evento("Aula de Javascript")

print(ev.nome)
print(ev2.nome)

ev.altera_nome_evento("Aula de Python com poo")
print(ev.nome)
