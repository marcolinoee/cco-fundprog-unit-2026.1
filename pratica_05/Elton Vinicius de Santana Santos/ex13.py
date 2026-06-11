nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for coluna in range(len(notas[0])):
    soma = 0

    for linha in range(len(notas)):
        soma += notas[linha][coluna]

    media = soma / len(notas)

    print("Avaliação", coluna, "- Média:", round(media, 2))

print("Resposta: O laço externo pode percorrer as colunas porque queremos calcular a média de cada avaliação, e cada coluna representa uma avaliação.")