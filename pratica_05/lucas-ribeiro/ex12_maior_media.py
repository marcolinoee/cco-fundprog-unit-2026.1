nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Resolução 1
cont = 0
maior_media = 0
melhor_aluno = ''
for linhas in notas:
    coluna = len(linhas)
    media = (sum(linhas))/coluna
    nome = nomes[cont]
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
    cont += 1

print(f'Maior média: {melhor_aluno} - {maior_media:.2f}')