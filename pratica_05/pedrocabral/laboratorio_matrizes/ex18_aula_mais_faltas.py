presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for j in range(len(presencas[0])):
    faltas = 0
    for i in range(len(presencas)):
        if presencas[i][j] == "F":
            faltas += 1
        elif presencas[i][j] != "P":
            print("erro")

    print(f"aula {j} teve {faltas} faltas", end=' ')
dados = [
    [1, 2],
    [3, 4]
]
print(dados[1][0])