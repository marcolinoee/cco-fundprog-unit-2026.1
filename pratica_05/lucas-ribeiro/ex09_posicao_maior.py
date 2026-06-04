numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]
maior = 0
linha_maior = 0
coluna_maior = 0
for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
            n = numeros[linha][coluna]
            if n > maior:
                maior = n
                linha_maior = linha
                coluna_maior = coluna
            else:
                continue

print(f'Maior valor: {maior}\nLinha: {linha_maior}\nColuna: {coluna_maior}')