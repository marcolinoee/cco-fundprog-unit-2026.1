valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma_valores = 0
for i in range(len(valores)):
    for j in range(len(valores[0])):
        soma_valores += valores[i][j]

print(f"soma total = {soma_valores}" )