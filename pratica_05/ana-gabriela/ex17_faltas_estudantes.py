presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    faltas = presencas[i].count("F")
    if faltas <= 1:
        situacao = "Frequência adequada"
    else:
        situacao = "Atenção à frequência"
    print(f"Estudante {i} - Faltas: {faltas} - {situacao}")