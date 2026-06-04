from os import system as s

lista_pares = []
for numero in range(8):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        continue
s('cls')
print(f'A soma dos números pares {lista_pares} é  igual a {sum(lista_pares)}')
