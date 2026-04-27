alunos = {
    'João': 7.5,
    'Maria': 8.0,
    'Pedro': 6.0,
    'Ana': 9.0,
    'Lucas': 5.5,
    'Anderson': 10.0
}

for i, (aluno, nota) in enumerate(alunos.items(), start=1):
    if nota >= 7.0:
        print(f"{i}. {aluno} e sua nota é {nota} - Aprovado")

    elif nota >= 4 and nota < 6.9:
        print(f"{i}. {aluno} e sua nota é {nota} - Recuperação")

    else:
        print(f"{i}. {aluno} e sua nota é {nota} - Reprovado")