def primo(numero):
    c = 1
    con = 0
    while c <= numero:
        if numero % c == 0:
            con += 1
        c += 1

    if con == 2 and numero != 1:
        return True
    else:
        return False


print(primo(2))
