valor_compra = float(input("Digite o valor da compra R$ "))
valor_frete = float(input("Digite o valor do frete R$ "))
fidelidade = input("Cliente cadastrado no programa fidelidade? 's'(sim) ou 'n'(não): ")
fidelidade = fidelidade.lower()
regra = valor_compra + valor_frete > 100 or fidelidade == 's'

print(f"Cupom pode ser utilizado? {regra}")
