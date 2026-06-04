tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[0])):
        print(tabuleiro[i][j], end=' ')
    print()