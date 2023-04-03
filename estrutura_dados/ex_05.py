alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

soma = 0
for i in alunos:
    soma = soma + i["nota"]

print(f"A média das notas de todos os alunos é {soma / len(alunos)}")
