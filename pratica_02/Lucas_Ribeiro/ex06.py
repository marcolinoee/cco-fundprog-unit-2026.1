from os import system as s

nota = float(input('Informe uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    s('cls')
    print('Nota inválida! Digite novamente...')
    nota = float(input('Informe uma nota de 0 a 10: '))
print('Obrigado por realizar a operação!')
