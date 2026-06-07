dados = [
    [1, 2],
    [3, 4]
]

# Código corrigido para exibir o valor 3:
print(dados[1][0])

# RESPOSTAS DA DEPURAÇÃO:
# 1. Qual erro ocorre? 
#    Ocorre um IndexError: list index out of range.
# 2. Por que o erro ocorre? 
#    Porque tentamos acessar o índice de linha 2 (dados[2][0]), mas a lista possui 
#    apenas as linhas 0 e 1.
# 3. Quais são os índices válidos de linha? 
#    Os índices válidos de linha são 0 e 1.
# 4. A correção foi implementada acima alterando dados[2][0] para dados[1][0].

# O que representa cada linha e cada coluna?
# Cada linha representa um grupo numérico indexado, e as colunas, itens de indexação interna de limite (0, 1).