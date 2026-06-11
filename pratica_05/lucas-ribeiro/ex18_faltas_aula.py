presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]



for linha in range(len(presencas)):
    cont_falta = 0 
    maior_falta = 0
    maior_faltas_aula = 0
    for coluna in range(len(presencas[0])):
        presenca = presencas[linha][coluna]
        if presenca == 'F':
            cont_falta += 1
        else:
            continue
        if cont_falta > maior_falta:
            maior_falta = cont_falta
            maior_faltas_aula = coluna
print(f'Aula com mais faltas {maior_faltas_aula} - Quantidade de faltas: {maior_falta}')