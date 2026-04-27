numeros = []

for numero in range(1, 11):
    usuario_input = input(f"Digite o número {numero}: ")
    numeros.append(int(usuario_input))

def parOuImpar(numeros):
    for numero in numeros:
        if numero > 0:
            print(f"{numero} é positivo.")
        elif numero == 0:
            print(f"{numero} é neutro.")
        else:
            print(f"{numero} é negativo.")

parOuImpar(numeros)