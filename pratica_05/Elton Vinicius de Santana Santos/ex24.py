nomes = ["Ana", "Bruno", "Carla", "Diego", "Eva"]

notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 4.5],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 5.5],
    [3.0, 4.0, 5.0, 4.5]
]

maior_media = 0
menor_media = 10

print("RELATÓRIO FINAL")

for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(nomes[i], "- Média:", round(media, 2), "-", situacao)

    if media > maior_media:
        maior_media = media

    if media < menor_media:
        menor_media = media

print("Maior média da turma:", round(maior_media, 2))
print("Menor média da turma:", round(menor_media, 2))