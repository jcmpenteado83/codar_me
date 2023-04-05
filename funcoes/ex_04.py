def maior_idade(pessoa):
    tipo = type(pessoa)
    if tipo == dict:
        if pessoa["idade"] >= 18:
            return print('A pessoa é maior de idade.')
        else:
            return print('A pessoa é menor de idade.')
    else:
        if pessoa[1] >= 18:
            return print('A pessoa é maior de idade.')
        else:
            return print('A pessoa é menor de idade.')

maior_idade(("João", 15))
maior_idade({"nome": "João", "idade": 18})
