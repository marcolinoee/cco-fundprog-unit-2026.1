nota = (int(input('Digite a nota do aluno: ')))
while nota < 0 or nota > 10:
    print ('Nota inválida. Digite novamente uma nota entre 0 e 10.')
    nota = (int(input('Digite a nota do aluno: ')))
print ('Nota válida. A nota do aluno é: ', nota)
