nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
cont = 0
for linhas in notas:
    coluna = len(linhas)
    media = (sum(linhas))/coluna
    situacao = ''
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Recuperação'
    print(f'{nomes[cont]} - Média: {media:.2f} - {situacao}')
    cont += 1
