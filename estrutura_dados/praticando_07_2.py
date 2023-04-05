pessoa = {}

pessoa["Nome"] = "Julio Cesar Manga Penteado"
pessoa["Endereços"] = [
    {
        "Tipo": "Principal",
        "Rua": "Joaquim José de Freitas",
        "Número": 718,
        "Bairro": "Centro",
        "Cidade": "Maringá",
        "Estado": "PR"
    },
    {
        "Tipo": "Comercial",
        "Rua": "Afonso Pena",
        "Número": 400,
        "Bairro": "Centro",
        "Cidade": "Maringá",
        "Estado": "PR"
    }
]
print(pessoa)
print(pessoa["Nome"])

for i in pessoa["Endereços"]:
    print(i)
