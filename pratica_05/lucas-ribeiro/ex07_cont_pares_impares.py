valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]
cont_par = 0
cont_impar = 0
for linha in valores:
    for n in linha:
        if n % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1

print(f'Números pares da matriz: {cont_par}\nNúmeros impares da matriz: {cont_impar}\n')


