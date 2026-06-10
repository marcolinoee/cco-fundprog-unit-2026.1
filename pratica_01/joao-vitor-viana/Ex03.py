print('Bem Vindo a Pizzaria Clean Code Clan!')

numero_fatias = int(input('Quantas fatias tem? '))
numero_progamadores = int(input('Quantas pessoas tem aí? '))

fatias_por_pessoa = numero_fatias // numero_progamadores
sobra = numero_fatias % numero_progamadores

print(f'Ficara {fatias_por_pessoa} fatias por pessoa e sobrará {sobra} fatias.')