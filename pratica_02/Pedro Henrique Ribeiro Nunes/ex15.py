maior = 0

for i in range(5):
    nota = float(input(f"Digite a {i+1}º nota: "))
    if nota > maior:
        maior = nota

print(f"A maior nota foi: {maior}")