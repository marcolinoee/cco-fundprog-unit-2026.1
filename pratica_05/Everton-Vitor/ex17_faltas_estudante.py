presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    faltas = presencas[i].count("F")
    
    # Desafio extra: Critério para frequência adequada (limite de 1 falta)
    if faltas <= 1:
        status = "Frequência adequada"
    else:
        status = "Atenção à frequência"
        
    print(f"Estudante {i} - Faltas: {faltas} -> {status}")

# O que representa cada linha e cada coluna?
# Cada linha armazena a totalidade de chamadas registradas de um único indivíduo matriculado.
# Cada coluna representa a verificação pontual feita em cada dia de aula.