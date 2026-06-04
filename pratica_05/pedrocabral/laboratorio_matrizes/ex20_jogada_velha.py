"""
Exercício 20 — Jogada simples no jogo da velha
Prática 05 — Laboratório de Matrizes
"""

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

def exibir_tabuleiro(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="")
            if j < len(m[i]) - 1:
                print(" | ", end="")
        print()
        if i < len(m) - 1:
            print("--+---+--")


exibir_tabuleiro(tabuleiro)

linha = int(input("Informe a linha (0 a 2): "))
coluna = int(input("Informe a coluna (0 a 2): "))
simbolo = input("Informe o símbolo (X ou O): ").strip().upper()

if simbolo != "X" and simbolo != "O":
    print("Símbolo inválido. Use apenas X ou O.")
elif linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
    print("Posição fora do tabuleiro.")
elif tabuleiro[linha][coluna] != " ":
    print("Posição ocupada. Escolha uma posição vazia.")
else:
    tabuleiro[linha][coluna] = simbolo
    print("Tabuleiro atualizado:")
    exibir_tabuleiro(tabuleiro)

# Comentário final: o que representa cada linha e cada coluna?
