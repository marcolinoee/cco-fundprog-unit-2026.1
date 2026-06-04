nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
media_alunos = []
print("boletim de medias:")
for i in range(len(notas)):
    soma_notas = 0
    for j in range(len(notas[0])):
        soma_notas += notas[i][j]
    media = soma_notas / len(notas[0])
    media_alunos.append(media)
    if media_alunos[i] >= 7.0:
        situacao = "aprovado"
    elif media_alunos[i] < 5.0:
        situacao = "reprovado"
    else:
        situacao = "recuperação"
    print(f"{nomes[i]}: {media_alunos[i]:.2f} - {situacao}")

