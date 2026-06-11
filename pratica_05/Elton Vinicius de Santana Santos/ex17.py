presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    faltas = 0

    for presenca in presencas[i]:
        if presenca == "F":
            faltas += 1

    print("Estudante", i, "- Faltas:", faltas)