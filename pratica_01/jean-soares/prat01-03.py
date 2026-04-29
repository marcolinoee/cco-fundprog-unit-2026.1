# Divisão Justa - Python

totalFatias = int(input("Digite o número total de fatias de pizza: "))
programadores = int(input("Digite o número de programadores na equipe: "))

fatiasPorPessoa = totalFatias // programadores
sobra = totalFatias % programadores

print("DIVISÃO:")
print(f"Total de fatias: {totalFatias}")
print(f"Número de programadores: {programadores}")
print(f"Fatias por pessoa: {fatiasPorPessoa}")
print(f"Fatias que sobram: {sobra}")