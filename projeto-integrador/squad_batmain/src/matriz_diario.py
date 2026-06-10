def calcular_media_aluno(n1, n2, n3):
    nome_aluno = str(input('Informe o nome do aluno(a): ').title())
    media_parcial = (n1*0.3) + (n2*0.3) + (n3*0.4)
    print(f'\nMédia parcial: {media_parcial:.1f}')

    if media_parcial >= 7:
        situacao = 'Aprovado'
        media_final = media_parcial
    elif media_parcial < 4:
        situacao = 'Reprovado'
        media_final = media_parcial
    else:
        print(f'\nO aluno(a) {nome_aluno} precisa fazer prova final!')
        prova_final = float(input('Digite a nota da prova final: '))
        media_final = (media_parcial + prova_final) / 2
    if media_final >= 5: 
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    print(f'A média final de {nome_aluno} é igual a: {media_final:.1f}')
    print(f'Situação: {situacao}')