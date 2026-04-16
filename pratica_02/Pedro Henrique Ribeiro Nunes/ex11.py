qtd = int(input('Digite a quantidade dee alunos: '))
for aluno in range(qtd):
    nota = float(input(f'Qual a nota do aluno {aluno + 1}? '))
    if nota >= 7 and nota <= 10:
        result = 'aprovado.'
        print(f'O aluno {qtd} está {result}')
    elif nota < 7 and nota >= 4:
        result = 'em recuperação.'
        print(f'O aluno {qtd} está {result}')
    elif nota >= 0 and nota < 4:
        result = 'reprovado.'
        print(f'O aluno {qtd} está {result}')
    else:
        print('Nota inválida.')
    