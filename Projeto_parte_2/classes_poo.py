class Lote:
    def __init__(self, numero, quantidade, data, custo_unitario):
        self.numero = numero
        self.quantidade = quantidade
        self.data = data
        self.custo_unitario = custo_unitario

    def __str__(self):
        return f"Lote {self.numero}: {self.quantidade} un, R$ {self.custo_unitario:.2f} ({self.data})"


class Produto:
    def __init__(self, codigo, nome, estoque_minimo):
        self.codigo = codigo
        self.nome = nome
        self.estoque_minimo = estoque_minimo
        self.lotes = []

    def adicionar_lote(self, quantidade, data, custo_unitario):
        numero = len(self.lotes) + 1
        lote = Lote(numero, quantidade, data, custo_unitario)
        self.lotes.append(lote)
        return lote

    def total_estoque(self):
        return sum(lote.quantidade for lote in self.lotes)

    def valor_total_estoque(self):
        return sum(lote.quantidade * lote.custo_unitario for lote in self.lotes)

    def esta_abaixo_estoque_minimo(self):
        return self.total_estoque() < self.estoque_minimo

    def __str__(self):
        return f"{self.codigo} - {self.nome} (Estoque: {self.total_estoque()}, Min: {self.estoque_minimo})"


def classificar_abc(produtos):
    if not produtos:
        return []

    ordenados = sorted(produtos, key=lambda p: p.valor_total_estoque(), reverse=True)
    total_geral = sum(p.valor_total_estoque() for p in ordenados)

    if total_geral == 0:
        return [(p, 'C', 0.0, 0.0) for p in ordenados]

    resultado = []
    acumulado = 0.0

    for p in ordenados:
        valor = p.valor_total_estoque()
        acumulado += valor
        perc_acum = (acumulado / total_geral) * 100

        if perc_acum <= 70:
            classe = 'A'
        elif perc_acum <= 90:
            classe = 'B'
        else:
            classe = 'C'

        resultado.append((p, classe, valor, perc_acum))

    return resultado
