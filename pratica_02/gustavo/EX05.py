contador_positivos = 0

for i in range(1, 11):
    numero = float(input("Digite o {}º número: ".format(i)))
    if numero > 0:
        contador_positivos += 1

print("Quantidade de números positivos: {}".format(contador_positivos))