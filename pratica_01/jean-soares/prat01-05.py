# Desafio do download - Python

tamanhoMB = float(input("Qual o tamanho do arquivo em MB? "))
velocidadeMbps = float(input("Qual a velocidade da sua internet em Mbps? "))

tamanhoBits = tamanhoMB * 8
tempoSegundos = tamanhoBits / velocidadeMbps

minutosInteiros = tempoSegundos // 60
segundosResto = tempoSegundos % 60

print("RESULTADO:")
print(f"O tempo total estimado é de: {minutosInteiros} minutos e {segundosResto} segundos.")
