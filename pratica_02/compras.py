total = 0

while True:
    compra = float(input("Digite o valor da compra: R$ "))
    total += compra

    continuar = input("Deseja continuar? (S/N): ")

    if continuar.upper() == "N":
        break

print(f"Total gasto: R$ {total:.2f}")