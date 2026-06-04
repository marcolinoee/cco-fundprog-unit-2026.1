nomes = ['Lucas', 'Vitor', 'João', 'Marcio', 'Maria']
notas = [
    [5.5, 7.8, 9.8, 3.5],
    [8.0, 7.5, 9.0, 6.6],
    [5.0, 6.0, 5.5, 7.9],
    [9.0, 8.5, 10.0, 9.0],
    [6.5, 7.0, 6.0, 4.3]
]
medias = []
alunos = []

situacao = ''
for nome in range(len(nomes)):
    soma = 0
    for nota in notas[nome]:
        coluna = len(notas[0])
        soma += nota
    media = (soma/coluna)
    medias.append(media)
    if media >= 7:
            situacao = 'Aprovado(a)'
    elif media >= 5 and media <= 7:
            situacao = 'Recuperação'
    else:
            situacao = 'Reprovado(a)'
    print(f'Aluno(a): {nomes[nome]} - Média: {media:.1f} - Situação: {situacao}')


maior_media = max(medias)
menor_media = min(medias)
print(f'Maior média: {maior_media:.1f}\nMenor média: {menor_media:.1f}')



    