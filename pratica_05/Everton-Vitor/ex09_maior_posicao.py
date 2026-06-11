numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior_valor = numeros[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior_valor:
            maior_valor = numeros[i][j]
            linha_maior = i
            coluna_maior = j

print(f"Maior valor: {maior_valor}")
print(f"Linha: {linha_maior}")
print(f"Coluna: {coluna_maior}")

# PERGUNTA OBRIGATÓRIA: por que foi necessário usar índices neste exercício?
# Resposta: Porque a proposta exige que informemos a exata localização geográfica do número (linha e coluna). 
# Iterando simplesmente por valor perderíamos o rastreio numérico de qual índice gerou o maior registro.

# O que representa cada linha e cada coluna?
# As linhas e colunas representam mapeamentos numéricos de uma grade bidimensional onde buscamos o valor topo.
