import os

# ============================================
# SISTEMA DE CUSTEIO ABC - POO
# ============================================

# ---- UTILITÁRIOS VISUAIS -------------------

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def linha(char="*", tamanho=45):
    print(char * tamanho)

def titulo(texto):
    print()
    linha()
    print(f"  {texto}")
    linha()
    print()

def subtitulo(texto):
    print()
    print(f"  >>> {texto}")
    linha("-", 45)

def separador():
    print()
    linha("=", 45)
    print()

# ============================================
# CLASSES
# ============================================

class Produto:
    def __init__(self, nome, preco, custo_direto, quantidade):
        self.nome = nome
        self.preco = preco
        self.custo_direto = custo_direto
        self.quantidade = quantidade
        self.direcionadores = {}
        self.custo_indireto_abc = 0.0

    def adicionar_direcionador(self, nome_atividade, consumo):
        self.direcionadores[nome_atividade] = consumo

    def receita_total(self):
        return self.preco * self.quantidade

    def custo_total(self):
        return (self.custo_direto * self.quantidade) + self.custo_indireto_abc

    def lucro(self):
        return self.receita_total() - self.custo_total()

    def margem_de_lucro(self):
        if self.receita_total() > 0:
            return (self.lucro() / self.receita_total()) * 100
        return 0.0

    def custo_unitario(self):
        if self.quantidade > 0:
            return self.custo_total() / self.quantidade
        return 0.0

    def exibir_resumo(self):
        print(f"\n  Produto : {self.nome}")
        linha("-", 45)
        print(f"  Preço de venda (unit.)  : R$ {self.preco:>10.2f}")
        print(f"  Custo direto (unit.)    : R$ {self.custo_direto:>10.2f}")
        print(f"  Quantidade produzida    :     {self.quantidade:>9}")
        print(f"  Custo indireto ABC      : R$ {self.custo_indireto_abc:>10.2f}")
        linha("-", 45)
        print(f"  Receita total           : R$ {self.receita_total():>10.2f}")
        print(f"  Custo total             : R$ {self.custo_total():>10.2f}")
        print(f"  Custo unitário          : R$ {self.custo_unitario():>10.2f}")
        print(f"  Lucro                   : R$ {self.lucro():>10.2f}")
        print(f"  Margem de lucro         :    {self.margem_de_lucro():>9.2f}%")


class Despesa:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Atividade:
    def __init__(self, nome):
        self.nome = nome
        self.despesas = []
        self.total_direcionador = 0.0

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)

    def definir_total_direcionador(self, total):
        self.total_direcionador = total

    def custo_total(self):
        return sum(d.valor for d in self.despesas)

    def taxa_direcionador(self):
        if self.total_direcionador == 0:
            return 0.0
        return self.custo_total() / self.total_direcionador

    def exibir_resumo(self):
        print(f"\n  Atividade : {self.nome}")
        linha("-", 45)
        for d in self.despesas:
            print(f"  Despesa: {d.nome:<20} R$ {d.valor:>8.2f}")
        linha("-", 45)
        print(f"  Custo total da atividade: R$ {self.custo_total():>8.2f}")
        print(f"  Taxa por direcionador   : R$ {self.taxa_direcionador():>8.2f}")


# ============================================
# CADASTRO DE PRODUTOS
# ============================================

limpar()
titulo("=== CADASTRO DE PRODUTOS ===")

produtos = []
qtd_produtos = int(input("  Quantos produtos deseja cadastrar? "))

for i in range(qtd_produtos):
    subtitulo(f"PRODUTO {i + 1}")
    nome = input("  Nome do produto          : ")
    preco = float(input("  Preço de venda (unit.)   : R$ "))
    custo_d = float(input("  Custo direto (unit.)     : R$ "))
    qtd = int(input("  Quantidade produzida     : "))
    produtos.append(Produto(nome, preco, custo_d, qtd))
    print(f"\n  ✔ {nome} cadastrado com sucesso!")

# ============================================
# CADASTRO DE DESPESAS
# ============================================

limpar()
titulo("=== CADASTRO DE DESPESAS ===")

despesas = []
qtd_despesas = int(input("  Quantas despesas deseja cadastrar? "))

for i in range(qtd_despesas):
    subtitulo(f"DESPESA {i + 1}")
    nome = input("  Nome da despesa  : ")
    valor = float(input("  Valor            : R$ "))
    despesas.append(Despesa(nome, valor))
    print(f"\n  ✔ Despesa '{nome}' cadastrada com sucesso!")

# ============================================
# CADASTRO DE ATIVIDADES
# ============================================

limpar()
titulo("=== CADASTRO DE ATIVIDADES ===")

atividades = []
qtd_atividades = int(input("  Quantas atividades deseja cadastrar? "))

for i in range(qtd_atividades):
    subtitulo(f"ATIVIDADE {i + 1}")
    nome = input("  Nome da atividade : ")
    atividade = Atividade(nome)

    print("\n  Despesas disponíveis:")
    for idx, d in enumerate(despesas):
        print(f"    [{idx}] {d.nome}  (R$ {d.valor:.2f})")

    indices_str = input("\n  Informe os números das despesas desta atividade (ex: 0,1): ")
    for num in indices_str.split(","):
        num = num.strip()
        if num.isdigit():
            atividade.adicionar_despesa(despesas[int(num)])

    atividades.append(atividade)
    print(f"\n  ✔ Atividade '{nome}' cadastrada com sucesso!")

# ============================================
# CONSUMO DAS ATIVIDADES POR PRODUTO
# ============================================

limpar()
titulo("=== CONSUMO DAS ATIVIDADES ===")

for atividade in atividades:
    subtitulo(f"ATIVIDADE: {atividade.nome.upper()}")
    total = 0
    for produto in produtos:
        consumo = int(input(f"  Consumo de {produto.nome:<20}: "))
        produto.adicionar_direcionador(atividade.nome, consumo)
        total += consumo
    atividade.definir_total_direcionador(total)

# ============================================
# CÁLCULO DO CUSTO INDIRETO ABC
# ============================================

for produto in produtos:
    custo_abc = 0.0
    for atividade in atividades:
        consumo = produto.direcionadores.get(atividade.nome, 0)
        custo_abc += consumo * atividade.taxa_direcionador()
    produto.custo_indireto_abc = custo_abc

# ============================================
# RESULTADO FINAL
# ============================================

limpar()
titulo("=== RESULTADO FINAL ===")

print("  RESUMO DOS PRODUTOS")
for produto in produtos:
    produto.exibir_resumo()

separador()

print("  RESUMO DAS ATIVIDADES")
for atividade in atividades:
    atividade.exibir_resumo()

separador()
print("  Cálculo concluído com sucesso!\n")