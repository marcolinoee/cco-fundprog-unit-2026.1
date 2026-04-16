fatia=int(input('Quantas fatias tem?'))
pessoas=int(input('Quantas Pessoas tem?'))
fatiasporpessoa = fatia // pessoas
sobra = fatiasporpessoa % pessoas

print(f'Cada pessoa ira comer {fatiasporpessoa} fatias,e sobrara {sobra} fatias')
