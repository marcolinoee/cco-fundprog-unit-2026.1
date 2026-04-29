fatia = int(input("Insira a quantidade de fatias: "))
pessoas = int(input("Insira a quantidade de programadores: "))
fatia_por_pessoa = fatia // pessoas
fatia_sobra = fatia % pessoas
print("Cada programador receberá " + str(fatia_por_pessoa) + " fatias de pizza.")
print("Sobrarão " + str(fatia_sobra) + " fatias de pizza")