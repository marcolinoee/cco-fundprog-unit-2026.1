notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for j in range(len(notas[0])):
    soma = 0
    for i in range(len(notas)):
        soma += notas[i][j]
    media = soma / len(notas)
    print(f"Avaliação {j} - Média: {media:.2f}")
