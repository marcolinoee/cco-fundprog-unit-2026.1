tamanho = float(input("qual o tamanho do arquivo em mb? "))
velocidade = float(input("qual a velocidade da sua internet em mbps? "))
dowload_time = tamanho * 8 / velocidade / 60
print(f"o tempo estimado para o download é de {dowload_time:.2f} minutos e {dowload_time * 60:.2f} segundos")