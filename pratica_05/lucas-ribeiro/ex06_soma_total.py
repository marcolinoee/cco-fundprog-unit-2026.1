valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]
soma = 0
for linha in valores:
    for n in linha:
        soma += n

print(f'Matriz: \n{valores[0]}\n{valores[1]}\n{valores[2]}\nSoma total dos valores: {soma}')