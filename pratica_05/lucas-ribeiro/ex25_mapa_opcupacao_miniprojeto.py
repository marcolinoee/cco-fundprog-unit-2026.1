def exibir_lab(lab, livres, ocupados, manutencao):
    for linha in lab:
        print(f'{' | '.join(linha)}\n{''.center(17,'=')}')
    livres = 0
    ocupados = 0
    manutencao = 0
    for linha in lab:
        for assento in linha:
            if assento == 'L':
                livres += 1
            elif assento == 'M':
                manutencao += 1
            else:
                ocupados += 1
    return livres, ocupados, manutencao


def main():
    
    lab = [['L' for coluna in range(5)] for linha in range(4)]
    lab[2][3] = 'M'
    lab[3][3] = 'O'
    lab[0][2] = 'M'
    lab[1][2] = 'O'

    cont_livres = 0
    cont_ocupados = 0
    cont_manutencao = 0

    print('Lista de ocupação do Laboratório 01:\n')
    cont_livres, cont_ocupados, cont_manutencao = exibir_lab(lab, livres=cont_livres, ocupados=cont_ocupados, manutencao=cont_manutencao)
    print(f'Livres: {cont_livres}\nEm Manutenção: {cont_manutencao}\nOcupados: {cont_ocupados}')
        
    try:
        linhas = int(input('Informe em qual linha deseja ocupar:  '))
        coluna = int(input('Digite em quam posição da linha deseja ocupar: '))
        if linhas > len(lab) - 1 or coluna > len(lab[0]) - 1:
            print('Assentos não encontrados!')
            
    except ValueError:
        print('[ERRO] Valores inválidos')
    

    posicao = lab[linhas][coluna]
    if posicao == 'O' or posicao == 'M':
        print('Posição ocupada ou em manutenção!')
    else:
        lab[linhas][coluna] = 'O'
        
    print('Lista de ocupação do Laboratório 01:\n')
    cont_livres, cont_ocupados, cont_manutencao = exibir_lab(lab, livres=cont_livres, ocupados=cont_ocupados, manutencao=cont_manutencao)
    print(f'Livres: {cont_livres}\nEm Manutenção: {cont_manutencao}\nOcupados: {cont_ocupados}')

main()
        




