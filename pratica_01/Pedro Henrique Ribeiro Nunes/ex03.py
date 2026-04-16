fatias = int(input('Qual o número de fatias? '))
pessoas = int(input('Qual a quantidade de programadores na equipe? '))
fatpes = fatias // pessoas
sobra = fatias % pessoas
print(f'Cada programador deverá comer {fatpes} fatias, sobrando {sobra} fatias.')
