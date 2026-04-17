contador = 0
soma = 0 
for i in range(8):
    num = int(input("Insira um número inteiro: "))
    if num%2 == 0:
        contador = contador + 1
        soma = soma + num
print("Soma dos números pares: " + str(soma))
print("Quantidade de números pares: " + str(contador))
