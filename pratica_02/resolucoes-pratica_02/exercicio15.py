maior_nota = 0

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    if nota > maior_nota:
        maior_nota = nota

print(f"A maior nota da turma foi: {maior_nota}")