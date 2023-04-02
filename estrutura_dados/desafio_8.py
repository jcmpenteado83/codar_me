lista = ["a", 5, {1}]

print(f"Lista original {lista}\n")

lista_invertida = []
for i in lista:
    lista_invertida.insert(0, i)

print(f"Lista invertida {lista_invertida}")
