nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")