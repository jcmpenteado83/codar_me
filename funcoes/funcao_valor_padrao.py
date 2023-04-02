def valor(consumo, servico=0.10, desconto=0.0):
    if servico == 0 and desconto == 0:
        return consumo
    else:
        valor_desconto = consumo * desconto
        valor_servico = consumo * servico
        total = (consumo - valor_desconto) + valor_servico
        return total


a = valor(consumo=100, servico=0.10, desconto=0.05)

print(a)
