nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"] 
notas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 6.0, 5.5, 4.0],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 5.5],
    [3.0, 4.0, 2.5, 3.5]
]

maior_media = -1
menor_media = 101
melhor = ""
pior = ""

for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nomes[i]} - Média = {media:.2f} -> {situacao}")
    if media > maior_media:
        maior_media = media
        melhor = nomes[i]
    if media < menor_media:
        menor_media = media
        pior = nomes[i]

print(f"\nMaior média -> {melhor} = {maior_media:.2f}")
print(f"Menor média -> {pior} = {menor_media:.2f}")