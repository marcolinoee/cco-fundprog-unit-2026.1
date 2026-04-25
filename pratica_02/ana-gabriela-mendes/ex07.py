soma = 0
for i in range(8):  
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos números pares é: {soma}")