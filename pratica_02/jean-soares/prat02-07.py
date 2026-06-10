# Soma de números pares - Python

somaPares = 0

for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    if numero % 2 == 0:
        somaPares += numero

print(f"A soma dos pares é: {somaPares}.")