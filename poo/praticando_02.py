class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basic", "premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")


cliente = Cliente("Julio", "jcmpenteado@gmail.com", "basic")
print(cliente.nome, cliente.email, cliente.plano)
cliente.mudar_plano("premium")
print(cliente.nome, cliente.email, cliente.plano)
