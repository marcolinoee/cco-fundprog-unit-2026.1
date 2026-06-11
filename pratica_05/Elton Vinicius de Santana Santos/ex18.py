presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

maior_faltas = 0
aula = 0

for coluna in range(len(presencas[0])):
    faltas = 0

    for linha in range(len(presencas)):
        if presencas[linha][coluna] == "F":
            faltas += 1

    if faltas > maior_faltas:
        maior_faltas = faltas
        aula = coluna

print("Aula com mais faltas:", aula)
print("Quantidade de faltas:", maior_faltas)