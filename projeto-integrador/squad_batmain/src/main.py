from menus_interface import verifica_notas, menu_opcao
from matriz_diario import calcular_media_aluno
from motor_alocacao import cadastrar_aula
from os import system as s

def clear():
    s('cls')
def main():
    n1 = 0
    n2 = 0
    n3 = 0
    while True:
        
        opcao = menu_opcao()

        if opcao == 1:
            clear()
            cadastrar_aula()
        elif opcao == 2:
            clear()
            n1 = verifica_notas('av1'.upper())
            n2 = verifica_notas('av2'.upper())
            n3 = verifica_notas('av3'.upper())
            calcular_media_aluno(n1, n2, n3)
        elif opcao == 0:
            clear()
            print('Sessão encerrada...\nAgradecemos por utilizar o nosso programa!')
            break
        else:
            print('[ERRO] Digite um valor entre 0, 1 e 2!')
            

main()
    
    