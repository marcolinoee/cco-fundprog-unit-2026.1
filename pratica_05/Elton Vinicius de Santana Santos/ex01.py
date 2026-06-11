matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()

print("Linhas:", len(matriz))
print("Colunas:", len(matriz[0]))