matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Linha {i} Coluna {j} Valor {matriz[i][j]}")

# PERGUNTA OBRIGATÓRIA: em que situações o percurso por índice é mais útil que o percurso por valor?
# Resposta: É mais útil quando precisamos modificar o valor daquela célula diretamente na matriz original, 
# quando precisamos exibir as coordenadas espaciais (coordenada de linhas/colunas) para o usuário, ou 
# quando relacionamos duas matrizes diferentes que compartilham as mesmas dimensões.

# O que representa cada linha e cada coluna?
# Cada linha representa a posição vertical 'i' na tabela de coordenadas.
# Cada coluna representa a posição horizontal 'j' na tabela de coordenadas.