total = 0
contador = 0
continuar = "S"

while continuar.upper() == "S":
    valor = float(input("Digite o valor da compra: R$ "))
    total += valor
    contador += 1
    continuar = input("Deseja continuar? (S/N): ")

print("=== RESUMO DAS COMPRAS ===")
print("Total de compras: {}".format(contador))
print("Valor total:      R$ {}".format(total))