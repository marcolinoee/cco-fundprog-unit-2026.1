quantidade = int(input("Digite a quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(1, quantidade + 1):
    media = float(input("Digite a média do {}º aluno: ".format(i)))
    
    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1

print("=== RESULTADO DA TURMA ===")
print("Aprovados:    {}".format(aprovados))
print("Recuperação:  {}".format(recuperacao))
print("Reprovados:   {}".format(reprovados))