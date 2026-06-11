valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0
impares = 0
pares_encontrados = []

for linha in valores:
    for valor in linha:
        if valor % 2 == 0:
            pares += 1
            pares_encontrados.append(valor)
        else:
            impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
print("Pares encontrados:", pares_encontrados)