nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
media_alunos = []
for i in range(len(notas)):
    soma_notas = 0
    for j in range(len(notas[0])):
        soma_notas += notas[i][j]
    media = soma_notas / len(notas[0])
    media_alunos.append(media)
print("boletim de medias:")
for i in range(len(nomes)):
    print(f"{nomes[i]}: {media_alunos[i]:.2f}")