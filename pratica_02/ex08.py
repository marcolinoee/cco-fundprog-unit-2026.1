n = int(input("Digite um número inteiro para calcular a tabuada: "))
print("Tabuada de " + str(n) + ":")
for i in range (1,11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))  