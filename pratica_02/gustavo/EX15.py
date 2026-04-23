maior = 0

for i in range(1, 6):
    nota = float(input("Digite a nota do {}º aluno: ".format(i)))
    if nota > maior:
        maior = nota

print("Maior nota da turma: {}".format(maior))