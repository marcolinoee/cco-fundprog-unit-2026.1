valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma = 0
for linha in valores:
    for coluna in linha:
        soma += coluna  
print("A soma de todos os elementos da matriz é:", soma)

media = soma / (len(valores) * len(valores[0]))
print("A média dos elementos da matriz é:", media)