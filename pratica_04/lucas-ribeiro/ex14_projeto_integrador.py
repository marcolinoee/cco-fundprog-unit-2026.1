def padronizacao_alunos(nomes_bruto, nomes_padronizada):
    nomes_padronizada = [nome.strip().title() for nome in nomes_bruto]
    return nomes_padronizada

def verifica_aprovados(medias_bruto, medias_aprovados):
    medias_aprovados = [media for media in medias_bruto if media >= 7]
    return medias_aprovados

def ata_de_presenca(alunos_presentes, consulta, situacao):
    
    for aluno in alunos_presentes:
        if aluno == consulta:
            situacao = True
        else:
            continue
    return situacao

def exibir_relatorio():
    nomes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
    nomes_padronizada = []
    nomes_padronizada = padronizacao_alunos(nomes_bruto, nomes_padronizada)
    medias_bruto = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
    medias_aprovados = []
    medias_aprovados = verifica_aprovados(medias_bruto, medias_aprovados)
    consulta = 'Lucas'
    situacao = False
    situacao = ata_de_presenca(nomes_padronizada, consulta, situacao)
    print(f'1) Padronizar nomes de estudantes\nNomes não padronizados: {nomes_bruto}\nNomes padronizados: {nomes_padronizada}\n\n2) Filtrar notas aprovadas\nNotas de todos os alunos: {medias_bruto}\nNotas dos alunos aprovados: {medias_aprovados}\n\n3) Verificação da presença de um nome consultado\nNomes na ata de presença: {nomes_padronizada}\nAluno consultado: {consulta}\nAluno está presente?: {situacao}')

exibir_relatorio()    
    
