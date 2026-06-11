presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

cont_presente = 0
cont_falta = 0
total_alunos = 0
for linha in presencas:
    for presenca in linha:
        if presenca == 'P':
            cont_presente += 1
            total_alunos += 1
        elif presenca == 'F':
            cont_falta += 1
            total_alunos += 1
        else:
            continue

print(f'Total de alunos na turma: {total_alunos}\nAlunos presentes: {cont_presente}\nAlunos com falta: {cont_falta}')
