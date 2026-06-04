nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

media_sala = []
for j in range(len(notas[0])):
    soma_notas = 0
    soma_notas += notas[0][j]
    soma_notas += notas[1][j]
    soma_notas += notas[2][j]
    soma_notas += notas[3][j]
    media = soma_notas / len(notas)
    media_sala.append(media)
    
    print(f"media da avaliacao {j+1}: {media:.2f}")