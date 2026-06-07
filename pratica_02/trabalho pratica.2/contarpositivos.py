contador_positivos = 0  # começa zerado antes do laço

for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero > 0:
        contador_positivos += 1  # só sobe se for positivo

print(f"Total de positivos: {contador_positivos}")