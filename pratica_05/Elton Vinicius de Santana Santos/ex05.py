matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("Linha", linha, "Coluna", coluna, "Valor", matriz[linha][coluna])


'''
O percurso por índice é mais útil quando precisamos saber a posição 
dos elementos na matriz ou alterar valores em posições específicas.

'''