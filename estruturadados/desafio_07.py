string = input("Digite uma palavra: ")

dicio = {}
for letra in string:
    if letra not in dicio:
        dicio[letra] = 1
    else:
        dicio[letra] += 1

print(dicio)

for letra, count in dicio.items():
    print(letra, count)
