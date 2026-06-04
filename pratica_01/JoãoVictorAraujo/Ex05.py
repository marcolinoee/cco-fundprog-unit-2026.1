contador_positivos = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    if numero > 0:
        contador_positivos += 1

print("Quantidade de positivos:", contador_positivos)
