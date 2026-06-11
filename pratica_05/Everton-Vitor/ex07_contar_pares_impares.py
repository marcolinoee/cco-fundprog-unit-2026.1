valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0
impares = 0
pares_encontrados = [] # Desafio extra

for linha in valores:
    for item in linha:
        if item % 2 == 0:
            pares += 1
            pares_encontrados.append(item)
        else:
            impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Lista de pares encontrados (Desafio): {pares_encontrados}")

# O que representa cada linha e cada coluna?
# Cada linha armazena três amostras numéricas coletadas.
# Cada coluna identifica a posição sequencial em que a amostra foi computada dentro do grupo.