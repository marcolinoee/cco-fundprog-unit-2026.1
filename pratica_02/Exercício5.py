contador_pos = 0

for i in range(0,10):
    num = float(input(f'Insira o {i+1}º número até que você tenha fornecido 10: '))

    if num > 0:
        contador_pos += 1
print(f'A quantidade de positivos é {contador_pos}')
