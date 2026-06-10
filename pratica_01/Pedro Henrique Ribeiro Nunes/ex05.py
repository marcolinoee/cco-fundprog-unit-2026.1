arqv = float(input('Qual o tamanho do arquivo, em MB? '))
vel = float(input('Qual o valor da velocidade, em Mbps? '))
tempo = arqv / (vel/8)
min = tempo // 60
seg = tempo - min*60
print(f'O arquivo demorará {min} minutos e {seg} segundos para terminar de baixar.')
