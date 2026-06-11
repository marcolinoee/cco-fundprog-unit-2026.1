presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for coluna in range(len(presencas[0])):
    cont_falta = 0 
    for linha in range(len(presencas)):
        presenca = presencas[linha][coluna]
        if presenca == 'F':
            cont_falta += 1
        else:
            continue
    print(f'Estudante {coluna} - Faltas: {cont_falta}')