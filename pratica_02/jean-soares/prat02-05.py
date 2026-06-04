# Contador de números positivos - Python

contadorPositivos = 0
for i in range (1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    
    if numero >= 0:
        contadorPositivos += 1

print(f"Total de números positivos: {contadorPositivos}")