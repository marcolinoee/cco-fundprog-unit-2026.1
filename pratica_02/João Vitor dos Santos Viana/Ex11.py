num_alunos = int(input('Informe o número de alunos: '))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(1, num_alunos + 1):
    media = float(input(f'Informe quanto foi a media do {i}º aluno: '))