from usuario import Usuario

class Administrador(Usuario):
    # def __init__(self, nome, email):
    #     super().__init__(nome, email)

    def imprime_usuario(self):
        if self.nome == 'Gabriel' and self.email == 'gabriel@exemplo.com':
            print(f'{self.nome}({self.email}) - Administrador')
        else:
            print(f'{self.nome}({self.email})')
