from flask import Flask
from evento_online import EventoOnline
from evento import Evento

app = Flask(__name__)

ev_online = EventoOnline("Live de Python")
ev_online2 = EventoOnline("Live de JavaScript")
ev_online3 = EventoOnline("Live de Ruby")
ev = Evento("Aula de Python", "Marigá-PR")
eventos = [ev_online, ev_online2, ev, ev_online3]


@app.route("/")
def index():
    return "<h1>Flask configurado com sucesso, né não!</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return eventos_dict
