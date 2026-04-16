positivos = []
negativos = []

for i in range(0, 10):
    numero = int(input('Digite um número: '))
    if(numero < 0):
        negativos.append(numero)
    elif(numero > 0):
        positivos.append(numero)
    else:
        print('0 é neutro')

print(positivos)
print(negativos)