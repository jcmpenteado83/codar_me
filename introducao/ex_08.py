n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
op = input("Escolha a operação: (+) (-) (/) (*)  : ")

if op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
elif op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
elif op == '/':
    if n2 == 0:
        print('Não é possível realizar divisão por zero!')
    else:
        print(f'{n1} / {n2} = {n1 / n2}')
elif op == '*':
    print(f'{n1} x {n2} = {n1 * n2}')
