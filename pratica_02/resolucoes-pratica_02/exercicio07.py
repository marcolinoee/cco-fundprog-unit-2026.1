soma_pares = 0

for i in range(0, 8):
    numero = int(input('Digite um número inteiro: '))
    if (numero % 2 == 0):
        soma_pares += numero

print(f'A soma dos pares foi {soma_pares}')