matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        valor = matriz[linha][coluna]
        print(f"linha: {linha}  coluna: {coluna} valor: {valor}")