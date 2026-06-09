qtd_alunos = int(input('Digite a quantidade de alunos: '))
aprovados = 0
recuperação = 0
reprovados = 0
for i in range(1, qtd_alunos + 1):
    nota = float(input(f'Digite a média do {i}º aluno: '))
    if nota >= 7:
        aprovados += 1
    elif nota >= 4 and nota < 7:
        recuperação += 1
    else:
        reprovados += 1
print(f'Número de alunos aprovados: {aprovados}')
print(f'Número de alunos em recuperação: {recuperação}')
print(f'Número de alunos reprovados: {reprovados}')
