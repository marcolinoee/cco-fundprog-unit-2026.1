arquivo_mb = float(input('Qual o tamanho do arquivo (MB): '))
velocidade_mbps = float(input('Informe a velocidade da sua internet (Mbps): '))

tempo_segundos  = arquivo_mb / (velocidade_mbps / 8)
minutos = tempo_segundos // 60
resto_segundos = tempo_segundos % 60

print(f'Download realizado em {minutos} minutos e {resto_segundos} segundos')
