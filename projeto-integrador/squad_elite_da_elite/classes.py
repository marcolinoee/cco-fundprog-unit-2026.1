class RegistroVenda:
    def __init__(self, data, produto, quantidade, valor_unitario, estado):
        self.data = data
        self.produto = produto
        self.quantidade = int(quantidade)
        self.valor_unitario = float(valor_unitario)
        self.estado = estado
        self.valor_total = self.quantidade * self.valor_unitario


class Dataset:
    def __init__(self):
        self.vendas = []

    def carregar_dados(self, dados_brutos):
        for item in dados_brutos:
            try:
                data, produto, qty, valor_uni, estado = item
                nova_venda = RegistroVenda(data, produto, qty, valor_uni, estado)
                self.vendas.append(nova_venda)
            except:
                print(f"Erro no registro: {item}. Pulando linha.")

    def calcular_analytics(self):
        vendas_estado = {}
        soma_total = 0

        for venda in self.vendas:
            if venda.estado in vendas_estado:
                vendas_estado[venda.estado] += venda.valor_total
            else:
                vendas_estado[venda.estado] = venda.valor_total
            soma_total += venda.valor_total

        print("\n--- Vendas por Estado ---")
        for estado, total in vendas_estado.items():
            print(f"{estado}: R$ {total:.2f}")

        total_vendas = len(self.vendas)
        ticket_medio = soma_total / total_vendas if total_vendas > 0 else 0
        print(f"\nTicket Médio Geral: R$ {ticket_medio:.2f}")
        
       
        return vendas_estado