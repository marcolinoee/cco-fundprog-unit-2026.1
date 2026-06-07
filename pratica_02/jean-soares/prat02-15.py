# Desafio da maior nota - Python

maior = -1

for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    
    if nota > maior:
        maior = nota

print(f"\nMaior nota encontrada: {maior}")