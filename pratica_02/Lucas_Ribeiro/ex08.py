numero = int(input('Digite um número inteiro para exibir sua tabuada completa: '))
for valor in range(1,11):
    print(f'{numero} x {valor} = {numero*valor}')