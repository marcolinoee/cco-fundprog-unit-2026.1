aluno = int(input("insira o número de alunos: "))
aprovados = 0
recuperacao = 0
reprovados = 0
for i in range (aluno):
    media = float(input("insira a média do aluno: "))
    if media >= 7:
        aprovados = aprovados + 1
    elif media >= 4:
        recuperacao = recuperacao + 1
    else:
        reprovados = reprovados + 1
print("Quantidade de alunos aprovados: " + str(aprovados))
print("Quantidade de alunos em recuperação: " + str(recuperacao))
print("Quantidade de alunos reprovados: " + str(reprovados))