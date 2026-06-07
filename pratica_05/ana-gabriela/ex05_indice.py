matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matriz)):        
    for j in range(len(matriz[i])):
        print("Linha", i, "Coluna", j, "Valor", matriz[i][j])

""" muito mais util quando se precisa acessar o valor de uma posição específica da matriz.