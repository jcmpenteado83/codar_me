i = 0
numero = list()
while i >= 0:
    num_user = int(input("[-1 para sair] Digite um número: "))
    if num_user < 0:
        break
    numero.append(num_user)
print(numero)
