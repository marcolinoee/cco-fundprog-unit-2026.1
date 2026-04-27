numeros = []

for numero in range(1, 9):
    usuario_input = input(f"Digite o número {numero}: ")
    numeros.append(int(usuario_input))

def parSoma(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f"A soma dos números pares é: {soma}")

parSoma(numeros)