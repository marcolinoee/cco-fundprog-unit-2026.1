nomes = ["filosofia", "matematica", "historia", "geografia"]
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]
    
aula_mais_faltas = 0
maior_faltas = 0

for j in range(len(presencas[0])):
    faltas = 0
    for i in range(len(presencas)):
        if presencas[i][j] == "F":
            faltas += 1
    if faltas > maior_faltas:
        maior_faltas = faltas
        aula_mais_faltas = j

print(f"Aula com mais faltas: {nomes[aula_mais_faltas]}")
print(f"Quantidade de faltas: {maior_faltas}")

print(f"Aula com mais faltas: {aula_mais_faltas}")
print(f"Quantidade de faltas: {maior_faltas}")