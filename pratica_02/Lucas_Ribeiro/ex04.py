from os import system as s

def clear():
    s('cls')

senha = str(input('Digite a senha de acesso: '))
while senha != 'acesso':
    clear()
    print('Acesso inválido! Digite novamnete...')
    senha = str(input('Digite a senha de acesso: '))
