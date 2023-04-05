palavra = input("Digite uma palavra: ")

dici = dict()
for i in palavra:
    if i not in dici:
        dici[i] = 1
    else:
        dici[i] += 1

print(dici)

for k, v in dici.items():
    print(k, v)
