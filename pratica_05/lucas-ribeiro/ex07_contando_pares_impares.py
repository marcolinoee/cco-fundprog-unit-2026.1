valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0
impares = 0 

for linha in valores:
    for n in linha:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f'Pares: {pares}\nImpares: {impares}')

