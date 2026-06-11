presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_presencas = 0
total_faltas = 0

for linha in presencas:
    for valor in linha:
        if valor == "P":
            total_presencas += 1
        else:
            total_faltas += 1

print("Total de presenças:", total_presencas)
print("Total de faltas:", total_faltas)
