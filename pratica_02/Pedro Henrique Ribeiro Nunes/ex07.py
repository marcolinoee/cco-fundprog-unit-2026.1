soma = 0
for num in range(8):
    nums = int(input(f'Digite o número {num + 1}: '))
    if nums % 2 == 0:
        soma += nums
print(f'A soma dos pares é igual a: {soma}')
