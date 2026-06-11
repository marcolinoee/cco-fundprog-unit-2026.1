matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Percorrendo diretamente por elemento (sem usar range ou índices)
for linha in matriz:
    for valor in linha:
        print(f"Valor: {valor}")

# O que representa cada linha e cada coluna?
# Cada linha representa um vetor numérico contido dentro da lista principal.
# Cada coluna representa uma unidade individual contida dentro deste vetor numérico.