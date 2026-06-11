nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

# Resolução 1
cont = 0
for linhas in notas:
    coluna = len(linhas)
    media = (sum(linhas))/coluna
    print(f'{nomes[cont]} - Média: {media:.2f}')
    cont += 1

# Resolução 2
for nome in range(len(nomes)):
    soma = 0
    for nota in notas[nome]:
        soma += nota
    media = soma / len(notas[1])
    print(f'{nomes[nome]} - Média: {media:.2f}')

            



            