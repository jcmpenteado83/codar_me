def fatorial(n):
    lista = list()
    while n > 0:
        lista.append(n)
        n -= 1

    na = 1
    for n in lista:
        na = na * n
    return na


print(fatorial(3))
