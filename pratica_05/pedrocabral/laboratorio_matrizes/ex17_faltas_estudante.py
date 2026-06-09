presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    faltas = 0

    for j in range(len(presencas[0])):
        if presencas[i][j] == "F":
            faltas += 1
        elif presencas[i][j] != "P":
            print("erro")

    print(f"estudante {i}: {faltas} faltas")
    if faltas in range(3):
        print("frequência adequada")
    else:
        print("atenção à frequência")
