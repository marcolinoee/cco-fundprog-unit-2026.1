total_gasto = 0

while True:
    compra = float(input("qual o valor da compra?  "))
    quantidade = int(input("qual a quantidade de produtos?  "))
    
    total = compra * quantidade
    total_gasto += total
    print(f"o valor total da compra é: R${total_gasto:.2f}")
    
    continuar = input("deseja continuar comprando? (s/n)  ")
    if continuar != "s":
        print("atendimento finalizado.")
        break
