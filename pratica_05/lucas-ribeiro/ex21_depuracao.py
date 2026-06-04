dados = [
    [1, 2],
    [3, 4]
]

# print(dados[2][0]) --> Erro

# 1) Qual o erro? -> O erro ocorre pois o programa não valida a posição na matriz
# 2) Por que o erro ocorre? -> Ocorre pelo fato da linha [2] não existir dentro da matriz
# 3) Quais os índices válidos de linha? -> A matriz "dados" contém apenas os índices 0 e 1
# 4) Exibindo o valor "3"
print(dados[1][0]) 