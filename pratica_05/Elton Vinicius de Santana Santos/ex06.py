valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma = 0
quantidade = 0

for linha in valores:
    for valor in linha:
        soma += valor
        quantidade += 1

media = soma / quantidade

print("Soma total:", soma)
print("Média geral:", media)