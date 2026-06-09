matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)

#o codigo printa uma matriz de [1, 0, 0] 3x

linha = 3
coluna = 3
matriz = [[0 for  coluna in range(coluna)] for linha in range(linha)]
matriz[1][0] = 1
print(matriz)