num_fatias = int(input('Qual é o número de fatias? '))
num_progs = int(input('Quantos programadores são? '))
fat_por_prog = num_fatias / num_progs
print('Cada programador pode comer', fat_por_prog, 'fatias de pizza.')
sobra = num_fatias % num_progs
print('Sobram', sobra, 'fatias de pizza.')
if sobra > 0:
        print('A pizza não foi dividida igualmente.')
        