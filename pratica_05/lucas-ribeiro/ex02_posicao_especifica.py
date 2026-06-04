# O valor da primeira linha e primeira coluna.
# O valor da segunda linha e terceira coluna.
# O valor da terceira linha e segunda coluna.
# A segunda linha completa.

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(f'Primeira linha e primeira coluna: {matriz[0][0]}\nSegunda linha e terceira coluna: {matriz[1][2]}\nTerceira linha e segunda coluna: {matriz[2][1]}\nSegunda linha completa: {matriz[1]}')

# Pergunta obrigatória no comentário final: por que matriz[1][2] não representa a primeira linha e segunda coluna?
# Isso ocorre pois tanto em listas quanto em matrizes as posições iniciam apartir do "0"