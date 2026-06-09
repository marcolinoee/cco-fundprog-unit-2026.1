alunos = int(input("Digite a quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(alunos):
    media = float(input(f"Digite a média do aluno {i+1}: "))
    if media >= 7:
        aprovados += 1
    elif media >=4 and media <= 6.9:
        recuperacao += 1
    else:        reprovados += 1
    
    print(f"Quantidade de alunos aprovados: {aprovados} ")
    
    print(f"Quantidade de alunos em recuperação: {recuperacao} ")
    
    print(f"Quantidade de alunos reprovados: {reprovados} ")