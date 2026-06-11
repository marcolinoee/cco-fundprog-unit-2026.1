def exibir_tabuleiro(tabuleiro):
    cont = 0
    for linha in tabuleiro:
        if cont == len(tabuleiro)-1:
            print(f'{' | '.join(linha)}\n')
        else:
            print(f'{' | '.join(linha)}\n{''.center(10,'-')}')
            cont += 1


tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]






