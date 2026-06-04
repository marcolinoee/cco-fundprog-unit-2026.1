num = int(input('Digite um numero para saber se é positivo ou negativo '))

if num < 0:
    print(f'o numero {num} é negativo')
elif num == 0:
    print('Voce digitou o numero zero')
else:
    print(f'o numero {num} é positivo')