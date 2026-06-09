contador_positivos = 0

print("Digite 10 números para análise:")

for rodada in range(1, 11): 
    numero = float(input(f"Digite o {rodada}º número: "))
    
    if numero > 0:
        contador_positivos += 1 

print("--- Resultado ---")
print(f"Você digitou {contador_positivos} números positivos.")