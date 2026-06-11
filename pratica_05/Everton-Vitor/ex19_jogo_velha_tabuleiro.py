tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

# --- DESAFIO EXTRA COM A FUNÇÃO SOLICITADA ---
def exibir_tabuleiro(t):
    for i in range(len(t)):
        # Imprime os elementos separados por uma barra vertical de formatação
        print(f" {t[i][0]} | {t[i][1]} | {t[i][2]} ")
        if i < len(t) - 1:
            print("-----------")

exibir_tabuleiro(tabuleiro)

# O que representa cada linha e cada coluna?
# Cada linha representa uma seção horizontal das jogadas do tabuleiro.
# Cada coluna define o encaixe vertical preciso das marcas do jogo (X, O ou espaços).