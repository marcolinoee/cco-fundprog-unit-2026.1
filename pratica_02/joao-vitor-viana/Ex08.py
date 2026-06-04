num = int(input('Digite o número que você quer saber a tabuada: '))

for i in range(1, 11):
    calculo = num * i
    tabuada = print(f'{num} X {i} = {calculo}')

print(f'Essa é a tabuada de {i}')