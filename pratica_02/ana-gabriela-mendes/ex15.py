nota = int(input("Digite a nota do aluno 1: "))
maior = nota

for i in range(1, 5):
    nota = int(input(f"Digite a nota do aluno {i + 1}: "))

if nota > maior:
    maior = nota

print(f"A maior nota foi: {maior}")