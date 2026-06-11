valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma_total = 0
total_elementos = 0

for linha in valores:
    for item in linha:
        soma_total += item
        total_elementos += 1

print(f"Soma total: {soma_total}")

# --- DESAFIO EXTRA ---
media = soma_total / total_elementos
print(f"Média geral: {media:.2f}")

# O que representa cada linha e cada coluna?
# Cada linha representa uma coleção de dados inteiros agrupados para amostragem.
# Cada coluna representa a entrada numérica individual pertencente à amostragem.