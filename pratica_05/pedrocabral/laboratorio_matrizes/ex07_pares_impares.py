valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0
impares = 0
for i in range(len(valores)):
    for j in range(len(valores[0])):
        if valores[i][j] % 2 == 0:
            pares +=1
        else:
            impares +=1
print(f"pares: {pares}")
print(f"impares: {impares}")

