def processar_venda(produto, quantidade_pedida):
    if quantidade_pedida <= 0:
        print("Erro: quantidade invalida.")
        return False

    estoque_total = produto.total_estoque()
    if estoque_total < quantidade_pedida:
        print(f"Erro: estoque insuficiente. Disponivel: {estoque_total}")
        return False

    pedido_original = quantidade_pedida
    lotes_baixados = []

    while quantidade_pedida > 0 and len(produto.lotes) > 0:
        lote = produto.lotes[0]

        if lote.quantidade <= quantidade_pedida:
            quantidade_pedida -= lote.quantidade
            lotes_baixados.append((lote.numero, lote.quantidade, 'total'))
            produto.lotes.pop(0)
        else:
            lote.quantidade -= quantidade_pedida
            lotes_baixados.append((lote.numero, quantidade_pedida, 'parcial'))
            quantidade_pedida = 0

    print(f"\n--- Venda de {pedido_original} unidades de {produto.nome} ---")
    for num, qtd, tipo in lotes_baixados:
        if tipo == 'total':
            print(f"  Lote {num}: {qtd} un (lote excluido)")
        else:
            print(f"  Lote {num}: {qtd} un (baixa parcial)")
    print(f"Estoque restante: {produto.total_estoque()}")

    if produto.esta_abaixo_estoque_minimo():
        print(f"\n*** ALERTA: Estoque de '{produto.nome}' abaixo do minimo! ***")

    return True
