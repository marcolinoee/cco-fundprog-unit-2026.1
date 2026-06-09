total = 0 

while True:
    valor = float(input("Digite o valor da compra: "))
    total += valor

    continuar = input("Deseja continuar (s/n): ")

    if continuar == "n":
        break
print("Total da compra:", total)