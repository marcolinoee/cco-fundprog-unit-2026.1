notas = []
for i in range(0 , 5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
print("maior nota:", max(notas))