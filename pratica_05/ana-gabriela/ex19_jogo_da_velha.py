tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

def exibir_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(" | ".join(tabuleiro[i]))
        if i < len(tabuleiro) - 1:
            print("---------")

exibir_tabuleiro(tabuleiro)