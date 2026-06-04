presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

P = 0
F = 0

for i in range(len(presencas)):
    for j in range(len(presencas[0])):
        if presencas[i][j] == "P":
            P += 1
        elif presencas[i][j] == "F":
            F += 1
            
        else:
            print("erro")
        
print(f"total de presenças: {P}")
print(f"total de faltas: {F}")
print(f"percentual de presença: {P / (P + F) * 100}%")