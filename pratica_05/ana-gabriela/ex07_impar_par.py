valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0
impares = 0
for linha in valores:
    for coluna in linha:
        if coluna % 2 == 0:
            pares += 1
        else:
            impares += 1    
print("Quantidade de números pares na matriz:", pares)
print("Quantidade de números ímpares na matriz:", impares)

pares_encontrados = []

for linha in valores:
    for valor in linha:
        if valor % 2 == 0:
            pares_encontrados.append(valor)

print("Números pares encontrados na matriz:", pares_encontrados)   