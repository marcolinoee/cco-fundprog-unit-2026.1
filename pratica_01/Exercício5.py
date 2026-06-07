tam_arqv = int(input('Insira o tamanho do arquivo em MB (Megabytes): '))
vel_internet = float(input('Insira a velocidade da internet em Mbps (Megabites por segundo): '))

tempo_seg = tam_arqv / (vel_internet / 8)
tempo_min = (tempo_seg // 60)
seg_restante = tempo_seg

print(f'O tempo de download será de {tempo_min} minutos e {tempo_seg} segundos')