presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_p = 0
total_f = 0

for linha in presencas:
    for valor in linha:
        if valor == "P":
            total_p += 1
        else:
            total_f += 1

total = total_p + total_f
print(f"Presenças: {total_p}")
print(f"Faltas: {total_f}")
print(f"Percentual de presença: {total_p/total*100:.1f}%")