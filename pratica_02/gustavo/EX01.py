numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número {} é positivo.".format(numero))
elif numero < 0:
    print("O número {} é negativo.".format(numero))
else:
    print("O número digitado é zero.")