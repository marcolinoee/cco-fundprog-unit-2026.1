tamanho_arquivo_mb=float(input('Qual o tamanho do arquivo em MB? '))
velocidade_internet_mbps=float(input('Qual a velocidade da sua internet em Mbps? '))
tempo_segundos = tamanho_arquivo_mb // (velocidade_internet_mbps // 8)
minutos_inteiros = tempo_segundos // 60
segundos_restantes = minutos_inteiros % tempo_segundos
print(f'Seu arquivo estara concluido em {minutos_inteiros} minutos e {segundos_restantes} segundos')