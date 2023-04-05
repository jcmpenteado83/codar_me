class Evento:
    def metodo_instancia(self):
        return ("método de instância camado", self)

    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)

    @staticmethod
    def metodo_estatico():
        return "estático chamado"

ev = Evento()
a = ev.metodo_instancia()
print(a)

b = Evento.metodo_classe()
# ou b = ev.metodo_classe()
print(b)

c = Evento.metodo_estatico()
# ou c = ev.metodo_estatico()
print(c)