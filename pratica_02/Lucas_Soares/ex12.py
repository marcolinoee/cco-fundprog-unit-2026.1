

while True:
    while True:
        try:
            valor = float(input("Digite o valor da compra: R$ "))
            
            if valor >= 0:
                break
            else:
                print("Valor inválido! Digite um valor positivo.")
        
        except ValueError:
            print("Entrada inválida! Digite um número.")

    

    
    while True:
        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        
        if continuar in ["S", "N"]:
            break
        else:
            print("Resposta inválida! Digite S ou N.")

    if continuar == "N":
        break

# print("\nResumo das compras:")
# print("Quantidade de compras:", quantidade)
# print("Total gasto: R$", total)