# Tabuada dinâmica - Python

numero = int(input("Digite um número  inteiro para ver a sua tabuada:"))
print(f"A tabuda do {numero} é:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")