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

linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))
simbolo = input("Digite o símbolo (X ou O): ")

if simbolo not in ["X", "O"]:
    print("Símbolo inválido.")
elif tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = simbolo
    print("Jogada realizada.")
else:
    print("Jogada inválida.")

exibir_tabuleiro(tabuleiro)