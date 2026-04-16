total_fatias = int(input('Digite o total de fatias: '))
total_pessoas = int(input('Digite o total de pessoas: '))

fatias_cada = total_fatias // total_pessoas
fatias_sobradas = total_fatias % total_pessoas

print(f'Para cada um terá {fatias_cada} fatias')
print(f'E terá {fatias_sobradas} fatias sobradas')