maior_nota = 0

for i in range(1, 6):
    nota = float(input(f'Insira a nota do {i}º aluno:'))

    if nota > maior_nota:
        maior_nota = nota
print('----' * 30)
print(f'A maior nota foi {maior_nota}!')