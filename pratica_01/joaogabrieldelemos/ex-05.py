tam_arq = float(input('Qual é o tamanho do arquivo em MB?'))
vel_internet = float(input('Qual é a velocidade da internet em Mbps?'))
tempo_seg = tam_arq / (vel_internet / 8)
tempo_min = tempo_seg / 60
seg_resto = tempo_seg % 60
print (f'O tempo estimado para baixar o arquivo é de {tempo_min} minutos e {seg_resto} segundos.')
