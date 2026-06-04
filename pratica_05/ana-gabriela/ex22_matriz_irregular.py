dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(len(dados[i])):  # usa o tamanho real de cada linha
        print(dados[i][j])