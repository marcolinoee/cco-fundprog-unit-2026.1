""""
1. Qual erro ocorre? aparece print(dados[2][0]) IndexError: list index out of range
com o dois em vermelho indicando que o indice 2 nao existe na lista dados.
2. Por que o erro ocorre? como o espaço na linha 0 em dados não ta no formato de sintaxe
correto, nao é considerado linha, entao é impossivel acessar dados[2][0] porque a 
linha 2 nao existe. 

"""
dados = [
    [2, 3],
    [1, 2],
    [3, 4]
]

print(dados[2][0])