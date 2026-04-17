contador_positivo = 0
for i in range(10):
    num = int(input("Insira um número inteiro: "))
    if num > 0:
        contador_positivo = contador_positivo + 1
print("Quantidade de números positivos: " + str(contador_positivo))