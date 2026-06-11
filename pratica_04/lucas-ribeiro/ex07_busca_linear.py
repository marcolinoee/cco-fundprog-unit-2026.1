estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"
validar = False

for nome in estudantes:
    if nome == procurado:
        validar = True
    else:
        continue

print(f'Nome do estudante procurado: {procurado}\nEstudante encontrado?: {validar}')