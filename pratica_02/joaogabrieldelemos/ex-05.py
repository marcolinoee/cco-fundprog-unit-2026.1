contador_positivos = 0

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 0:
        contador_positivos += 1

print(f"Você digitou {contador_positivos} números positivos.")
