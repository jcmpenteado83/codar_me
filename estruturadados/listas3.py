notas = [8, 9, 10, 7.5, 4, 6]

i = 0
total = 0
while i < len(notas):
    total = total + notas[i]
    i += 1

print(f"O total das notas é {total}")
print(f"A média das notas é {total / len(notas)}")
