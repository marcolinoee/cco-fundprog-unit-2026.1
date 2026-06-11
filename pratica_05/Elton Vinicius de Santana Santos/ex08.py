numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
menor = numeros[0][0]

linha_maior = 0
coluna_maior = 0

linha_menor = 0
coluna_menor = 0

for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
        valor = numeros[linha][coluna]

        if valor > maior:
            maior = valor
            linha_maior = linha
            coluna_maior = coluna

        if valor < menor:
            menor = valor
            linha_menor = linha
            coluna_menor = coluna

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Posição do maior:", linha_maior, coluna_maior)
print("Posição do menor:", linha_menor, coluna_menor)