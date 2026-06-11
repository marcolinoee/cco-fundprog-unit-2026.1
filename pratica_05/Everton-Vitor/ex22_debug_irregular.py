dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

# Versão corrigida que percorre com segurança total usando o tamanho real de cada sublista
for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])

# PERGUNTA OBRIGATÓRIA: por que range(3) não é seguro nesse caso?
# Resposta: Porque a matriz é irregular. A segunda linha (dados[1]) possui apenas 2 elementos 
# (índices 0 e 1). Se fixarmos range(3), o programa tentará acessar dados[1][2], que não existe, 
# gerando um erro de quebra (IndexError).

# O que representa cada linha e cada coluna?
# Cada linha representa um vetor de dados heterogêneo quanto ao tamanho.
# Cada coluna representa a entrada contida sob o limite dinâmico de sua própria linha.