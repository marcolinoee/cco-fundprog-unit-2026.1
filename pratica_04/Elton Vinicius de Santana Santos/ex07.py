estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

for estudante in estudantes:
    if estudante == procurado:
        print(f"{procurado} encontrado!")
        break
else:
    print(f"{procurado} não encontrado!")