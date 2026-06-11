notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

qtd_alunos = len(notas)
qtd_avaliacoes = len(notas[0])

# Percorrendo as colunas no laço externo
for col in range(qtd_avaliacoes):
    soma_avaliacao = 0
    for lin in range(qtd_alunos):
        soma_avaliacao += notas[lin][col]
        
    media_col = soma_avaliacao / qtd_alunos
    print(f"Avaliação {col} - Média: {media_col:.2f}")

# PERGUNTA OBRIGATÓRIA: por que neste exercício o laço externo pode percorrer as colunas?
# Resposta: Porque o objetivo é acumular valores verticalmente. Fixando a coluna no laço externo, 
# podemos variar as linhas no laço interno para somar as notas que todos os alunos tiraram naquela mesma prova.

# O que representa cada linha e cada coluna?
# Cada linha representa um estudante diferente avaliado.
# Cada coluna representa uma avaliação fixa, unificando os dados das notas sob um mesmo critério de prova.