valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]
soma_total = 0
for linha in range(len(valores)):
    soma_total += sum(valores[linha])



print(f'Soma total: {soma_total}')