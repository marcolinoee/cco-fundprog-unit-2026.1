presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_p = 0
total_f = 0

for linha in presencas:
    for registro in linha:
        if registro == "P":
            total_p += 1
        elif registro == "F":
            total_f += 1

print(f"Total de presenças: {total_p}")
print(f"Total de faltas: {total_f}")

# --- DESAFIO EXTRA ---
total_geral = total_p + total_f
pct_presenca = (total_p / total_geral) * 100
print(f"Percentual geral de presença da turma: {pct_presenca:.2f}%")

# O que representa cada linha e cada coluna?
# Cada linha representa a ficha de frequência total de um aluno específico.
# Cada coluna representa um dia letivo de aula específico em ordem cronológica.