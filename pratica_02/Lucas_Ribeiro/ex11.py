from os import system as s

numero_alunos = int(input('Informe a quantidade total de alunos: '))

aprovados = 0
recuperacao = 0
reprovados = 0

for validar_nota in range(numero_alunos):
    media = float(input(f'Digite a média do aluno {validar_nota+1}: '))
    if media >= 7:
        aprovados += 1
    elif media >= 4 and media <= 6.9:
        recuperacao += 1
    else:
        reprovados += 1
s('cls')
print(f'A quantidade de Aprovados foi de {aprovados} alunos\nDos em Recuperação foram de {recuperacao} alunos\nE para os Reprovados é de {reprovados} alunos')


