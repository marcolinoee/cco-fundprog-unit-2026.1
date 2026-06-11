def exibir_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])

        if i < len(tabuleiro) - 1:
            print("---------")

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

exibir_tabuleiro(tabuleiro)