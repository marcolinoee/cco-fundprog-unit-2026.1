matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Exibindo linha por linha
for linha in matriz:
    print(linha)

# Quantidade de linhas e colunas
qtd_linhas = len(matriz)
qtd_colunas = len(matriz[0])

print(f"Linhas: {qtd_linhas}")
print(f"Colunas: {qtd_colunas}")

# --- DESAFIO EXTRA ---
print("\nMatriz no formato de tabela:")
for linha in matriz:
    for item in linha:
        print(f"{item:<4}", end="")
    print() # Quebra de linha ao fim de cada linha da matriz

# O que representa cada linha e cada coluna?
# Cada linha representa um grupo horizontal de números sequenciais na estrutura de dados.
# Cada coluna representa a posição vertical correspondente dentro de cada uma dessas linhas.