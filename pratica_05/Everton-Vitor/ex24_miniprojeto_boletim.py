# 1 e 2. Armazenamento de dados iniciais
nomes = ["Amanda", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Cada linha = um estudante; cada coluna = uma nota das suas 4 avaliações
notas = [
    [8.5, 7.0, 9.0, 8.0],
    [5.5, 6.0, 5.0, 6.5],
    [4.0, 5.5, 3.5, 4.5],
    [9.0, 9.5, 10.0, 9.0],
    [7.0, 6.5, 7.0, 8.0]
]

relatorio_estudantes = []
maior_media = -1
nome_maior = ""
menor_media = 11
nome_menor = ""

# 3 e 4. Cálculo de médias e classificações
for i in range(len(notas)):
    media_aluno = sum(notas[i]) / len(notas[i])
    
    if media_aluno >= 7.0:
        situacao = "Aprovado"
    elif media_aluno >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    # Armazena as informações tratadas em uma lista de dicionários ou sublistas
    relatorio_estudantes.append([nomes[i], media_aluno, situacao])
    
    # 6 e 7. Controle da maior e menor média da turma
    if media_aluno > maior_media:
        maior_media = media_aluno
        nome_maior = nomes[i]
    if media_aluno < menor_media:
        menor_media = media_aluno
        nome_menor = nomes[i]

# 5. Exibição estruturada do relatório final
print("====================================================")
print("             BOLETIM ESCOLAR FINAL                  ")
print("====================================================")
print(f"{'NOME':<15} | {'MÉDIA':<7} | {'SITUAÇÃO':<12}")
print("----------------------------------------------------")
for aluno in relatorio_estudantes:
    print(f"{aluno[0]:<15} | {aluno[1]:<7.2f} | {aluno[2]:<12}")
print("----------------------------------------------------")
print(f"Maior média da turma: {nome_maior} ({maior_media:.2f})")
print(f"Menor média da turma: {nome_menor} ({menor_media:.2f})")
print("====================================================")

# O que representa cada linha e cada coluna?
# Cada linha representa o registro escolar integral indexado de um estudante de Amanda a Eduardo.
# Cada coluna representa a nota obtida em um dos 4 Bimestres do ano letivo.