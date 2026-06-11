numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
linha_maior = 0
coluna_maior = 0

for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
        if numeros[linha][coluna] > maior:
            maior = numeros[linha][coluna]
            linha_maior = linha
            coluna_maior = coluna

print("Maior valor:", maior)
print("Linha:", linha_maior)
print("Coluna:", coluna_maior)

'''
Foi necessário usar índices porque precisávamos descobrir a linha e a coluna onde o maior valor estava localizado na matriz.
'''