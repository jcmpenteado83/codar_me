def dois_args(lista, elemento):
    t = 0
    for i in lista:
        if i == elemento:
            t += 1
    if t >= 1:
        return True
    else:
        return False


print(dois_args([1, 2, 9, 10], 9))
