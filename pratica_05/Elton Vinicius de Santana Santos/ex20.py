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

linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))
simbolo = input("Digite o símbolo (X ou O): ")

if tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = simbolo
else:
    print("Jogada inválida")

exibir_tabuleiro(tabuleiro)