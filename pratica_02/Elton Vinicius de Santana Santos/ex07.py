lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

def numero_par():
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

print("Soma dos pares:", numero_par())