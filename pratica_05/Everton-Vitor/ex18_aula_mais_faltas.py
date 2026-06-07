presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

qtd_aulas = len(presencas[0])
qtd_alunos = len(presencas)

aula_campea_faltas = -1
max_faltas = -1

for col in range(qtd_aulas):
    faltas_desta_aula = 0
    for lin in range(qtd_alunos):
        if presencas[lin][col] == "F":
            faltas_desta_aula += 1
            
    if faltas_desta_aula > max_faltas:
        max_faltas = faltas_desta_aula
        aula_campea_faltas = col

print(f"Aula com mais faltas: {aula_campea_faltas}")
print(f"Quantidade de faltas: {max_faltas}")

# O que representa cada linha e cada coluna?
# Cada linha mapeia os históricos de alunos em registros de chamada individuais.
# Cada coluna unifica a listagem de presença do dia da aula.
