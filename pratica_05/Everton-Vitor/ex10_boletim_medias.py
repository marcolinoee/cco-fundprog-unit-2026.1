nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for i in range(len(notas)):
    soma_notas = sum(notas[i])
    media = soma_notas / len(notas[i])
    # Desafio extra: formatado com duas casas decimais usando :.2f
    print(f"{nomes[i]} - Média: {media:.2f}")

# O que representa cada linha e cada coluna?
# Cada linha representa o histórico escolar (conjunto de notas) de um estudante específico.
# Cada coluna representa a nota de uma atividade específica feita por todos eles.