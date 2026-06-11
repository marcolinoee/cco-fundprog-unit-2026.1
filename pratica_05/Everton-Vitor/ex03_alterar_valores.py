notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0]
]

print("Matriz antes da alteração:")
for linha in notas:
    print(linha)

# Alterando valores específicos
notas[1][0] = 6.5
notas[2][2] = 9.5

print("\nMatriz depois da alteração:")
for linha in notas:
    print(linha)

# --- DESAFIO EXTRA ---
print("\n--- Atualização customizada ---")
l = int(input("Digite a linha (0 a 2): "))
c = int(input("Digite a coluna (0 a 2): "))
val = float(input("Digite o novo valor da nota: "))

if 0 <= l < len(notas) and 0 <= c < len(notas[0]):
    notas[l][c] = val
    print("Célula atualizada com sucesso! Nova matriz:")
    for linha in notas:
        print(linha)
else:
    print("Índices fora dos limites permitidos!")

# O que representa cada linha e cada coluna?
# Cada linha representa o conjunto de notas de um estudante específico.
# Cada coluna representa a nota obtida em uma determinada avaliação (Avaliação 0, 1 e 2).