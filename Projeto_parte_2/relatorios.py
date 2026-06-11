def relatorio_inventario(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\n" + "=" * 85)
    print("RELATORIO DE INVENTARIO GERAL")
    print("=" * 85)

    for produto in produtos:
        print(f"\nProduto: {produto.codigo} - {produto.nome}")
        print(f"Estoque Total: {produto.total_estoque()} | Minimo: {produto.estoque_minimo}")
        print("-" * 85)
        print(f"{'Lote':<8} {'Quantidade':<12} {'Data':<14} {'Custo Un.':<14} {'Total Lote':<14}")
        print("-" * 85)
        for lote in produto.lotes:
            total_lote = lote.quantidade * lote.custo_unitario
            print(f"{lote.numero:<8} {lote.quantidade:<12} {lote.data:<14} R$ {lote.custo_unitario:<9.2f} R$ {total_lote:<9.2f}")
        print("=" * 85)


def relatorio_abc(produtos):
    from classes_poo import classificar_abc

    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    classificacao = classificar_abc(produtos)
    total_geral = sum(p.valor_total_estoque() for p in produtos)

    print("\n" + "=" * 75)
    print("CURVA ABC - CLASSIFICACAO POR VALOR EM ESTOQUE")
    print("=" * 75)
    print(f"{'Produto':<20} {'Valor Estoque':<18} {'% Individual':<15} {'% Acumulada':<15} {'Classe':<6}")
    print("-" * 75)

    for produto, classe, valor, perc_acum in classificacao:
        perc_ind = (valor / total_geral * 100) if total_geral > 0 else 0
        nome_exib = produto.nome[:19]
        print(f"{nome_exib:<20} R$ {valor:<11.2f} {perc_ind:>6.2f}%      {perc_acum:>5.1f}%      {classe}")

    print("=" * 75)
    print(f"Valor total em estoque: R$ {total_geral:.2f}")

    cont_a = sum(1 for _, c, _, _ in classificacao if c == 'A')
    cont_b = sum(1 for _, c, _, _ in classificacao if c == 'B')
    cont_c = sum(1 for _, c, _, _ in classificacao if c == 'C')
    print(f"Classe A: {cont_a} itens | Classe B: {cont_b} itens | Classe C: {cont_c} itens")


def relatorio_ponto_pedido(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    abaixo = [p for p in produtos if p.esta_abaixo_estoque_minimo()]

    print("\n" + "=" * 60)
    print("PONTO DE PEDIDO - ITENS ABAIXO DO ESTOQUE MINIMO")
    print("=" * 60)

    if not abaixo:
        print("Nenhum produto abaixo do estoque minimo.")
        return

    print(f"{'Produto':<20} {'Estoque Atual':<16} {'Minimo':<10}")
    print("-" * 60)
    for p in abaixo:
        print(f"{p.nome:<20} {p.total_estoque():<16} {p.estoque_minimo:<10}")
    print("=" * 60)
