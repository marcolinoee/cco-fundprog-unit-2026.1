tam = float(input("Insira o tamanho do arquivo em MB: "))
vel = float(input("Insira a velocidade de download em Mbps: "))
ts = (tam * 8) / vel
min = int(ts // 60)
seg = int(ts % 60)
print("O tempo estimado para download é de " + str(min) + " minutos e " + str(seg) + " segundos.")  