tamanho_mb = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_mbps = float(input("Digite a velocidade da internet em Mbps: "))

tempo_segundos = tamanho_mb / (velocidade_mbps / 8)
minutos_inteiros = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

print("Tempo estimado: {} minutos e {} segundos.".format(minutos_inteiros, segundos_restantes))