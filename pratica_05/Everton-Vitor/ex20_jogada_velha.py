tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

lin = int(input("Digite a linha da jogada (0 a 2): "))
col = int(input("Digite a coluna da jogada (0 a 2): "))
simbolo = input("Digite o símbolo (X ou O): ").upper()

# Desafio extra: Impedir símbolos diferentes de X e O
if simbolo != "X" and simbolo != "O":
    print("Jogada inválida! Símbolo não permitido.")
else:
    # Verificação básica de limites e se a célula está vazia
    if 0 <= lin < 3 and 0 <= col < 3:
        if tabuleiro[lin][col] == " ":
            tabuleiro[lin][col] = simbolo
            print("Jogada realizada com sucesso!")
        else:
            print("Jogada inválida: Posição já ocupada!")
    else:
        print("Jogada inválida: Coordenadas fora do tabuleiro!")

print("\nTabuleiro Atual:")
for linha in tabuleiro:
    print(linha)

# O que representa cada linha e cada coluna?
# Cada linha e cada coluna representam as coordenadas geográficas cartesianas que demarcam o tabuleiro.