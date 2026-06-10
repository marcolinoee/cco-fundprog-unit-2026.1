contador_de_pares = 0
for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        contador_de_pares += 1
print(f"A quantidade de números pares é: {contador_de_pares}")
        
