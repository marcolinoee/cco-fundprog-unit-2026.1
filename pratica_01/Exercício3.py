fatias = int(input('Insira o número de fatias da pizza: '))
pessoas = int(input('Insira o número de pessoas na equipe: '))

fatias_pessoa = fatias // pessoas
sobra = fatias % pessoas

print(f'O total de fatias inteiras que cada um comerá são {fatias_pessoa}. O resto que sobrará na caixa é {sobra}')