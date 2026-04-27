tamanhoDoArquivo = int(input("Digite o tamanho do arquivo em MB: "))
velocidadeDaInternet = int(input("Digite a velocidade da internet em Mbps: "))

tempoDeDownload = (tamanhoDoArquivo * 8) / velocidadeDaInternet
segundos = tempoDeDownload % 60
minutos = (tempoDeDownload // 60) % 60
print(f"Tempo estimado de download: {int(minutos)} minutos e {int(segundos)} segundos")