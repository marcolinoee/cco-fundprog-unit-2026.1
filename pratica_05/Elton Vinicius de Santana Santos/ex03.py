notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0]
]

for linha in notas:
    print(linha)

notas[1][0] = 6.5
notas[2][2] = 9.5

print()

for linha in notas:
    print(linha)