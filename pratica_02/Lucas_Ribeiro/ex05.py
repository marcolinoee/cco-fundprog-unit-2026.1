from os import system as s

filtrar_inteiro = []
for numero in range(10):
    numero = float(input('Digite um número: '))
    if numero > 0:  
        filtrar_inteiro.append(numero)
    else:
        continue
s('cls')
print(f'Números inteiros filtrados: {filtrar_inteiro}')