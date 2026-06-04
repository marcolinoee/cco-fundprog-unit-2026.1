# Classificação de turma - Python

quantAlunos = int(input("Digite a quantidade de alunos: "))
aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(1, quantAlunos + 1):
    media = float(input(f"Digite a média do {i}º aluno: "))

    if media >= 7:
        aprovados += 1

    elif media < 7 and media >= 4:
        recuperacao += 1

    else:
        reprovados += 1

print(f"Total de alunos: {quantAlunos}")
print(f"Estão aprovados: {aprovados}")
print(f"Estão de recuperação: {recuperacao}")
print(f"Estão reprovados: {reprovados}")

    