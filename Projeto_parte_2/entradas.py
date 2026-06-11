def ler_int_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Erro: valor nao pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um numero inteiro valido.")


def ler_float_positivo(mensagem):
    while True:
        try:
            valor_str = input(mensagem).replace(',', '.')
            valor = float(valor_str)
            if valor < 0:
                print("Erro: valor nao pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um numero valido.")


def cadastrar_produto(produtos):
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = input("Codigo do produto: ").strip()
    for p in produtos:
        if p.codigo == codigo:
            print("Erro: codigo ja cadastrado.")
            return None

    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: nome nao pode ser vazio.")
        return None

    estoque_minimo = ler_int_positivo("Estoque minimo: ")

    from classes_poo import Produto
    produto = Produto(codigo, nome, estoque_minimo)

    resp = input("Deseja cadastrar um lote inicial? (s/n): ").strip().lower()
    while resp == 's':
        cadastrar_lote(produto)
        resp = input("Cadastrar outro lote? (s/n): ").strip().lower()

    return produto


def cadastrar_lote(produto):
    print(f"\n--- NOVO LOTE para {produto.nome} ---")
    qtd = ler_int_positivo("Quantidade: ")
    if qtd == 0:
        print("Erro: quantidade precisa ser maior que zero.")
        return None

    data = input("Data (DD/MM/AAAA): ").strip()
    custo = ler_float_positivo("Custo unitario (R$): ")

    lote = produto.adicionar_lote(qtd, data, custo)
    print(f"Lote {lote.numero} cadastrado com sucesso!")
    return lote
