
from os import system as s

def clear():
    s('cls')

def subtrair(val1,val2):
    return val1-val2

def somar(val1,val2):
    return val1+val2

def main():
    menu = '''
       ===== Seja Bem Vindo(a) ao menu interativo =====

       Selecione uma das seguintes opções:
       [1] Somar
       [2] Subtrair
       [0] Sair      

 ==>   '''

    while True:
        opcoes = input(menu)
        if opcoes == '1':
            clear()
            num1 = float(input('Digite um número para somar: '))
            num2 = float(input('Digite outro número para somar: '))
            print(f'A soma entre {num1} e {num2} é {somar(num1,num2)}')
        elif opcoes == '2':
            clear()
            num1 = float(input('Digite um número para subtrair: '))
            num2 = float(input('Digite outro número para subtrair: '))
            print(f'A subtração entre {num1} e {num2} é {subtrair(num1,num2)}')
        elif opcoes == '0':
            break
        else: 
            print('Operação falhou! Operação selecionada não encontrada...')


main()