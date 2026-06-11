matriz = [[0] * 3]  * 3
matriz[0][0] = 1
print(matriz)
# No caso acima é criada uma matriz que adiciona 3 linhas e colunas com o valor "0". Em seguida o valor matriz[0][0] é alterado para "1", que também altera os valores da coluna 0 para 1

matriz_2 = [[0 for coluna in range(3)] for linha in range(3)]
matriz_2[0][0] = 1
print(matriz_2)
# Neste segundo caso apenas alteramos o valor de uma célula, sendo apenas na posição [0][0] da matriz_2. Isso ocorre neste caso pois temos a criação de listas para cada linha, o que não é o caso da primeira versão