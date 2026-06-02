print("="*50)
print("tempo estimado de download solicitando")
print("="*50)

Tamanho_MB = float(input("Qual o Tamanho do arquivo (MB): "))
Velocidade_Mbps = float(input("Qual a Velocidade da Internet (Mbps): "))

velocidade_MB_por_segundo = Velocidade_Mbps / 8
Tempo_Segundos = Tamanho_MB / velocidade_MB_por_segundo

Minutos_Inteiro = int(Tempo_Segundos // 60)
Segundos_Restantes = int(Tempo_Segundos % 60)

print(f"{Minutos_Inteiro} minutos e {Segundos_Restantes} segundos")