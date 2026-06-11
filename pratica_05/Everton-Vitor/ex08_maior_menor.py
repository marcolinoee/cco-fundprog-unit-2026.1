numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

# Inicializa o maior e o menor com o primeiro elemento válido da matriz
maior_valor = numeros[0][0]
menor_valor = numeros[0][0]

pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior_valor:
            maior_valor = numeros[i][j]
            pos_maior = (i, j)
        if numeros[i][j] < menor_valor:
            menor_valor = numeros[i][j]
            pos_menor = (i, j)

print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Desafio - Posição do maior: Linha {pos_maior[0]}, Coluna {pos_maior[1]}")
print(f"Desafio - Posição do menor: Linha {pos_menor[0]}, Coluna {pos_menor[1]}")

# O que representa cada linha e cada coluna?
# Cada linha representa uma das subdivisões numéricas da coleção.
# Cada coluna representa um valor isolado contido nestas subdivisões.