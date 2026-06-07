
def menu_principal():
        print('=============================================================')
        print('                     [ERP EDUCACIONAL]  ')
        print('=============================================================')
        print('[1] ALOCAÇÃO DE PROFESSOR/TURMAS')
        print('[2] DIÁRIO DE CLASSE')
        print('[0] Encerrar\n')
        print('=============================================================')
        
        
def menu_opcao():
    while True:
        try:
            menu_principal()
            menu = int(input('Escolha uma das opções: ').strip())
            if menu < 0 or menu > 2:
                 print('[ERRO] Informe um número entre as opção a seguir')
                 continue
            return menu
        except ValueError:
                print("[ERRO] Digite apenas números!")
                continue
def verifica_notas(nome_avaliacao):
    while True:
        try:
            valor = float(input(f"Digite a nota da {nome_avaliacao} (0 a 10): "))
            if valor >= 0 and valor <= 10:
                return valor
            print("[ERRO] A nota deve estar entre 0 e 10")
        except ValueError:
            print("[ERRO] Valor invalido! Digite um numero")