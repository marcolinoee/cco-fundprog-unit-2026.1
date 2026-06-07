numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = 0
linha_maior = 0
coluna_maior = 0

for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior:
            maior = numeros[i][j]
            linha_maior = i
            coluna_maior = j    
print("Maior número na matriz:", maior)
print("Posição do maior número: Linha", linha_maior, "Coluna", coluna_maior)   

