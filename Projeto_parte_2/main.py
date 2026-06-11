from classes_poo import Produto
from entradas import cadastrar_produto, cadastrar_lote
from motor_vendas import processar_venda
from relatorios import (
    relatorio_inventario,
    relatorio_abc,
    relatorio_ponto_pedido,
)


def listar_produtos(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    print("\n--- PRODUTOS CADASTRADOS ---")
    for i, p in enumerate(produtos, 1):
        print(f"{i}. {p}")


def selecionar_produto(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return None

    listar_produtos(produtos)
    try:
        idx = int(input("\nSelecione o numero do produto: ")) - 1
        if 0 <= idx < len(produtos):
            return produtos[idx]
        else:
            print("Indice invalido.")
            return None
    except ValueError:
        print("Entrada invalida.")
        return None


def menu_principal():
    produtos = []

    while True:
        print("\n" + "=" * 45)
        print("SISTEMA DE GESTAO DE ESTOQUE - PEPS")
        print("=" * 45)
        print("1. Cadastrar produto")
        print("2. Entrada de lote (nota fiscal)")
        print("3. Realizar venda (PEPS)")
        print("4. Relatorio de inventario")
        print("5. Curva ABC")
        print("6. Ponto de pedido")
        print("7. Listar produtos")
        print("0. Sair")
        print("-" * 45)

        opcao = input("Escolha: ").strip()

        if opcao == '1':
            produto = cadastrar_produto(produtos)
            if produto:
                produtos.append(produto)
                print(f"Produto '{produto.nome}' cadastrado com sucesso!")

        elif opcao == '2':
            if not produtos:
                print("Cadastre um produto primeiro.")
                continue
            p = selecionar_produto(produtos)
            if p:
                cadastrar_lote(p)

        elif opcao == '3':
            if not produtos:
                print("Cadastre um produto primeiro.")
                continue
            p = selecionar_produto(produtos)
            if p:
                print(f"Estoque atual: {p.total_estoque()}")
                try:
                    qtd = int(input("Quantidade a vender: "))
                    processar_venda(p, qtd)
                except ValueError:
                    print("Entrada invalida.")

        elif opcao == '4':
            relatorio_inventario(produtos)

        elif opcao == '5':
            relatorio_abc(produtos)

        elif opcao == '6':
            relatorio_ponto_pedido(produtos)

        elif opcao == '7':
            listar_produtos(produtos)

        elif opcao == '0':
            print("Encerrando sistema...")
            break

        else:
            print("Opcao invalida.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()
