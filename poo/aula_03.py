# declarando uma classe
class Evento:
    def altera_nome_evento(self, novo_nome):
        print("Alterando o nome do evento para")
        self.nome = novo_nome

#variável + Classe = Cria um Objeto do tipo Evento com um evento/simbolo apontando para ele
# instanciar uma classe
ev = Evento()
ev.nome = "Aula de Python"
print(ev.nome)

ev.altera_nome_evento("Aula de JavaScript")
print(ev.nome)
