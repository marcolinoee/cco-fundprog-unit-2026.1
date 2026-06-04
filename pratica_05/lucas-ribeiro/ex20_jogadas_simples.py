from ex19_jogo_da_velha import exibir_tabuleiro

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", ""]
]

print(f'Tabuleiro atual:\n')
exibir_tabuleiro(tabuleiro)
try:
    linha_jogada = int(input('Digite a linha para a jogada: '))
    coluna_jogada = int(input('Digite em qual coluna será a jogada: '))
    if linha_jogada > (len(tabuleiro) - 1) or coluna_jogada > (len(tabuleiro) - 1):
        print('Posições inválidas! Digite um posição existente no tabuleiro.')
    simbolo_jogada = str(input('informe com qual símbolo deseja realizar a jogada [X] [O]:  '))
    if simbolo_jogada != 'X' or simbolo_jogada != 'O':
        print('Símbolo inválido! Digite apenas [X] ou [O]')
except ValueError:
    print('Valores inválidos!')
posicao_jogada = tabuleiro[linha_jogada][coluna_jogada]
if posicao_jogada == 'X' or posicao_jogada == 'O':
    print('Jogada inválida! A jogada nesta posição já foi realizada anteriormente')
else:
    tabuleiro[linha_jogada][coluna_jogada] = simbolo_jogada
    print('Jogada realizada com sucesso!')
    print(f'\nTabuleiro atualizado:\n')
    exibir_tabuleiro(tabuleiro)
