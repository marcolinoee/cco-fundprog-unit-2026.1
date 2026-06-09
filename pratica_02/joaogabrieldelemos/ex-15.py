maior_nota = 0
print('Digite as 5 notas dos alunos')

for i in range(1, 6):
    nota = float(input(f'Digite a {i}ª nota: '))
    if nota > maior_nota:
        maior_nota = nota
print(f'A maior nota da turma foi: {maior_nota}')
