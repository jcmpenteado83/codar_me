usuarios = {"alice", "bob", "carlos"}
usuarios_2 = set(["alice", "bob", "lucas"])

print(usuarios.union(usuarios_2))
print(usuarios.intersection(usuarios_2))
print(usuarios.difference(usuarios_2))

e_igual = usuarios.union(usuarios_2) == usuarios | usuarios_2
print(e_igual)
e_igual = usuarios.intersection(usuarios_2) == usuarios & usuarios_2
print(e_igual)
e_igual = usuarios.difference(usuarios_2) == usuarios - usuarios_2
print(e_igual)
