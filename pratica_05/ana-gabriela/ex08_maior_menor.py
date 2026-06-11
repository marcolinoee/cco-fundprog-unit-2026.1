numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

if numeros:
    maior = numeros[0][0]
    menor = numeros[0][0]

    for linha in numeros:
        for coluna in linha:
            if coluna > maior:
                maior = coluna
            if coluna < menor:
                menor = coluna

    print("Maior número na matriz:", maior)
    print("Menor número na matriz:", menor)

    