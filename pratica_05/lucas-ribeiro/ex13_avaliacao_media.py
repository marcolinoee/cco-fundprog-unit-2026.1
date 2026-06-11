nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 6.0, 5.5, 7.0],
    [9.0, 8.5, 10.0, 4.5],
    
    
    
]


for coluna in range(len(notas[0])):
    soma = 0 
    for linha in range(len(notas)):
        soma += notas[linha][coluna]
    media = (soma / len(notas))
    print(f'Avaliação {coluna} - Média: {media:.1f}')

# Pergunta Obrigatória
# Utilizei o laço externo para a resolução deste exercício pois para a contagem de cada coluna é necessário o uso de um laço para limitar ao número de colunas da matriz de notas