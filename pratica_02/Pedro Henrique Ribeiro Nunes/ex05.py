contador = 0
for num in range(10):
    nums = int(input(f'Digite o número {num + 1}: '))
    if nums > 0:
        contador += 1
print(f'Quantidade de números postivos: {contador}')
