lista_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {num}:")
for i in lista_tabuada:
    resultado = num * i
    print(f"{num} x {i} = {resultado}")