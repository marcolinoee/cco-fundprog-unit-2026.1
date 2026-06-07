matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(f"1. Primeira linha e primeira coluna: {matriz[0][0]}")
print(f"2. Segunda linha e terceira coluna: {matriz[1][2]}")
print(f"3. Terceira linha e segunda coluna: {matriz[2][1]}")
print(f"4. Segunda linha completa: {matriz[1]}")

# PERGUNTA OBRIGATÓRIA: por que matriz[1][2] não representa a primeira linha e segunda coluna?
# Resposta: Porque a indexação em Python começa em 0. Portanto, matriz[1][2] acessa a SEGUNDA linha 
# (índice 1) e a TERCEIRA coluna (índice 2). A primeira linha e segunda coluna seriam acessadas por matriz[0][1].

# O que representa cada linha e cada coluna?
# Cada linha representa uma sublista indexada de 0 a 2.
# Cada coluna representa um elemento interno dessa sublista, também indexado de 0 a 2.