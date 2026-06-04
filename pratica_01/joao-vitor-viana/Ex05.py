tamanho_arqv = float(input('Qual é o tamnaho do arquivo (Mbps)? '))
velocidade = float(input('Qual é a velocidade da internet? '))

tempo_s = tamanho_arqv / (velocidade / 8)
minutos = tempo_s // 60
segundos_restantes = tempo_s % 60

print(f'{minutos} minutos e {segundos_restantes} segundos')