alunos = {
    'João': 7.5,
    'Maria': 8.0,
    'Pedro': 6.0,
    'Ana': 9.0,
    'Lucas': 5.5,
}

def exibir_alunos():
    for i, (aluno, nota) in enumerate(alunos.items(), start=1):
        print(f"{i}. {aluno} e sua nota é {nota}")

exibir_alunos()
print("")
print(f"A maior foi a de {max(alunos, key=alunos.get)} com nota {max(alunos.values())}")