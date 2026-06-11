produto = "Notebook"
estoque_minimo = 15

lote001_qtd = 20
lote002_qtd = 50

print(f"Entrada e Saída: {produto}")
print(f"Estoque inicial - Lote001: {lote001_qtd} - Lote002: {lote002_qtd}")


quantidade_pedida = int(input("Digite a quantidade pedida: "))

estoque_total = lote001_qtd + lote002_qtd 

if quantidade_pedida > estoque_total:
    print("ERRO: Quantidade pedida maior que quantidade total.")
else:
    print("Pedido sendo processado...")

    while quantidade_pedida > 0:
        if lote001_qtd > 0:
            if lote001_qtd >= quantidade_pedida:
                print(f"{quantidade_pedida} unidades do Lote 001 sendo separadas...")
                lote001_qtd -= quantidade_pedida
                quantidade_pedida = 0
            else:
                print(f"Separando {lote001_qtd} unidades do Lote 001, Lote esgotado.")
                quantidade_pedida -= lote001_qtd
                lote001_qtd = 0
        elif lote002_qtd > 0:
            if lote002_qtd >= quantidade_pedida:
                print(f"{quantidade_pedida} unidades do Lote 002 sendo separadas...")
                lote002_qtd -= quantidade_pedida
                quantidade_pedida = 0
            else:
               print(f"Separando {lote002_qtd} unidades do Lote 002, Lote esgotado.") 
               quantidade_pedida -= lote002_qtd
               lote002_qtd = 0
        else:
            break
print ('Pedido concluído!')
print("--- Resumo do Estoque Pós-Venda ---")
print(f"Lote 001: {lote001_qtd} unidades")
print(f"Lote 002: {lote002_qtd} unidades")

novo_estoque_total = lote001_qtd + lote002_qtd
if novo_estoque_total < estoque_minimo:
    print(f"Novo estoque total ({novo_estoque_total}) está abaixo do mínimo ({estoque_minimo})! Fazer pedido de novas unidades")