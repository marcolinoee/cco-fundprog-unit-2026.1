notas = [
    [6.0, 7.0, 6.7],
    [5.0, 8.0, 9.0],
    [7.0, 6.0, 8.0]
]
print("============================")
for i in range(3):
    print(notas[i])
print("============================")
notas[1][0] = 6.5
notas[2][2] = 9.0
print("============================")
print("atualizado")
for i in range(3):
    print(notas[i])
print("============================")

print("adicione uma coluna e uma linha nova de notas:")
notas[0].append((input("adicione a nota da nova coluna: ")))
notas[1].append((input("adicione a nota da nova coluna: ")))
notas[2].append((input("adicione a nota da nova coluna: ")))
print("============================")
print("atualizado(dnv)")
for i in range(3):
    print(notas[i])
