alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9)
]

soma = 0
for i in alunos:
    soma = soma + i[1]

print(f"A média das notas de todos os alunos é {soma / len(alunos)}")
