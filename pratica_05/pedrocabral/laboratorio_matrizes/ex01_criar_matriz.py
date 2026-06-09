aura = [
    [0, 6, 7],
    [0, 6, 9],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        print(aura[i][j], end=' ')
    print()
    
    colunas = len(aura)
    linhas = len(aura[0])
print(f'colunas: {colunas}')
print(f'linhas: {linhas}')
