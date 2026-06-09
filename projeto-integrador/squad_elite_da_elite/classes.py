def calcularAnalytics(dados):
    vendas_estado = {}

    for item in dados:
        
        data, produto, quantidade, valor_unitario, estado = item
        valor = quantidade * valor_unitario 

        if estado in vendas_estado:
            vendas_estado[estado] += valor
        else:
            vendas_estado[estado] = valor  

    print("\n--- Vendas por Estado  --- ")
    for estado, total in vendas_estado.items():
        print(f"{estado}: R$ {total:.2f}")

    # Calcular ticket médio
    soma_total = 0
    quantidade_total = 0

    for item in dados:
        data, produto, quantidade, valor_unitario, estado = item
        soma_total += quantidade * valor_unitario
        quantidade_total += quantidade

    ticket_medio = soma_total / quantidade_total if quantidade_total > 0 else 0
    print(f"\nTicket Médio: R$ {ticket_medio:.2f}")

    return vendas_estado
