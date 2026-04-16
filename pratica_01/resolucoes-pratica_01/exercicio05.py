# Considere que 1 Byte = 8 bits.
tamanho_mb = float(input('Diga o tamanho do arquivo em Megabytes (MB): '))
vel_net = float(input('Diga a velocidade da internet em Megabits por segundo (Mbps)'))

tempo_segundos = tamanho_mb / (vel_net / 8)
minutos_Inteiros = tempo_segundos // 60
segundos_Restantes = tempo_segundos % 60

print(f'{minutos_Inteiros} minutos e {segundos_Restantes} segundos')