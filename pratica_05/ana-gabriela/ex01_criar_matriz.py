matriz_caixas = [
    [10, 9, 6],
    [2, 5, 3],
    [8, 4, 7]
]

for linha in matriz_caixas:
    for coluna in linha:
        print(coluna, end=' ')
    print()

print("Linhas:", len(matriz_caixas))
print("Colunas:", len(matriz_caixas[0]))
