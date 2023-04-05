def maior_numero(lista):
    numeros = lista
    maior = max(numeros)
    posicao = numeros.index(maior)
    tupla = (posicao, maior)
    return tupla


print(maior_numero([4, 39, 1, 1, 2, 10]))
