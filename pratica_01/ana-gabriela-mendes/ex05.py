TamanhoArquivo = int(input("Digite o tamanho do arquivo em megabytes: "))
VelocidadeDownload = int(input("Digite a velocidade de download em megabits por segundo: "))
TempoEstimado = TamanhoArquivo / (VelocidadeDownload/8)
MinutosInteiros = int(TempoEstimado // 60)
SegundosRestantes = TempoEstimado % 60
print(f"O tempo estimado para o download é de {MinutosInteiros} minutos e {SegundosRestantes:.2f} segundos.")
