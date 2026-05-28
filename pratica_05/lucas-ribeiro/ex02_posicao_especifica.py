matriz = [
    [10, 20, 30, 50],
    [40, 50, 60, 60],
    [70, 80, 90, 30]
]

print(f'Linha 1 e coluna 1: {matriz[0][0]}\nLinha 2 e coluna 3: {matriz[1][2]}\nLinha 3 e coluna 2: {matriz[2][1]}\nLinha 2 completa: {matriz[1]}')
# A matriz[1][2] não representa a linha 1 e a coluna 2 pois na matriz se inicia em 0, portanto, tanto a linha quanto coluna tem como posição 1 o 0