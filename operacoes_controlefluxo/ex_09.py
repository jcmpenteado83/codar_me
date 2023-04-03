usuario = input("Usuário: ")
senha = input("Senha: ")

user = "admin"
passw = "123123"

if usuario == user and senha == passw:
    print("Autenticação foi bem sucedida!")
elif usuario != user:
    print("Usuário inexistente!")
elif senha != passw:
    print("Senha incorreta!")
