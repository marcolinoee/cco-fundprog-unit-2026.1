numero_fatias = int(input('Informe o número total de fatias: '))
numero_pessoas = int(input('Digite quantas pessoasm compõem a equipe: '))

fatias_por_pessoa = numero_fatias // numero_pessoas
sobra_fatias = numero_fatias % numero_pessoas

print(f'A quantidade de fatias por pessoa é {fatias_por_pessoa} e a  sobre é {sobra_fatias}')