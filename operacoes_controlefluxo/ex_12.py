n1 = int(input("Digite um número:\n"))

c = 1
con = 0
while c <= n1:
    if n1 % c == 0:
        con += 1
    c += 1

if con == 2 and n1 != 1:
    print("É UM NÚMERO PRIMO")
else:
    print("NÃO É UM NÚMERO PRIMO")
