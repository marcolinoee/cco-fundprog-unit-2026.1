lista_notas = []

for aluno in range(5):
    nota = float(input(f'Informe a nota do aluno {aluno+1}: '))
    lista_notas.append(nota)
maior = max(lista_notas)
print(f'A maior nota entres os alunos é {maior}')