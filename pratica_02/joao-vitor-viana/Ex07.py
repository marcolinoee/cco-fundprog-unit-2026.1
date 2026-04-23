soma_pares = 0

for i in range(1,9):
    numero = int(input(f'Digite o {i}º numero inteiro: '))

    if numero % 2 == 0:
        soma_pares += numero
print('----' * 8)
print(f'A soma dos números pares digitados é: {soma_pares}')