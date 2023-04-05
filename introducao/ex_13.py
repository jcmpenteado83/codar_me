print("\n##### Tente adivinhar meu número. Você tem 3 tentativas! #####\n")

num = 6

cont = 1
while cont <= 3:
    escolha = int(input("Tente adivinhar meu número: "))
    if escolha == num:
        print("O número é igual!")
        print("Voce Ganhou")
        break
    elif escolha < num:
        print("O número é menor que o meu.\n")
    elif escolha > num:
        print("O número é maior que o meu.")
    cont += 1

if cont == 4:
    print("VOCE PERDEU")
