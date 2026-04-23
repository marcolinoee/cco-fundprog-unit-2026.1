soma_pares = 0

for i in range(1, 9):
    numero = int(input("Digite o {}º número: ".format(i)))
    if numero % 2 == 0:
        soma_pares += numero

print("Soma dos números pares: {}".format(soma_pares))