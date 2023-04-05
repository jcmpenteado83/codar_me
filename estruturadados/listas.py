notas = [8, 10, 8.5]

print(notas[2])
notas.append(9)
print(notas[3])
print(notas)
notas.sort(reverse=True)
print(notas)

notas.pop(0)
print(notas)

notas.insert(0, 8)

print(notas)