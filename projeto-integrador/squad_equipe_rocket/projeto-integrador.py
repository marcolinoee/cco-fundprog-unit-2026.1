# INGRESSO DE DADOS - JEAN SOARES

# Parte do menu interativo:
def exibir_menu():
    print("\n" + "=" * 45)
    print("DASHBOARD FINANCEIRO - SISTEMA CONTÁBIL")
    print("=" * 45)
    print("(1) Inserir dados de um ano")
    print("(2) Sair")
    print("=" * 45)

# Parte da coleta/validação de dados:
def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("AVISO: Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Erro! Valor inválido. Digite apenas números (ex: 150000).")


def coletar_dados():
    while True:
        print("\n" + "=" * 45)
        print("INSERÇÃO DE DADOS - BALANÇO PATRIMONIAL")
        print("=" * 45)

        print("\nATIVOS:")
        ativo_circulante = ler_valor("Ativo Circulante: R$ ")
        estoques         = ler_valor("Estoques: R$ ")
        ativo_nao_circ   = ler_valor("Ativo Não Circulante: R$ ")
        ativo_total      = ativo_circulante + ativo_nao_circ
        print(f"-> Ativo Total: R$ {ativo_total}")

        print("\nPASSIVOS:")
        passivo_circulante = ler_valor("Passivo Circulante:     R$ ")
        passivo_nao_circ   = ler_valor("Passivo Nao Circulante: R$ ")
        passivo_total      = passivo_circulante + passivo_nao_circ
        print(f"-> Passivo Total: R$ {passivo_total}")

        print("\nPATRIMÔNIO LÍQUIDO:")
        patrimonio_liquido = ler_valor("Patrimonio Liquido: R$ ")

        print("\nDRE:")
        receita_liquida = ler_valor("Receita Liquida: R$ ")
        lucro_liquido   = ler_valor("Lucro Liquido: R$ ")

        # Parte da validação de ouro:
        soma_passivo_pl = passivo_total + patrimonio_liquido

        if ativo_total != soma_passivo_pl:
            print("\n" + "!" * 45)
            print("ERRO FATAL: Balanço não fecha!")
            print(f"Ativo Total: R$ {ativo_total}")
            print(f"Passivo Total + PL: R$ {soma_passivo_pl}")
            print("Verifique os valores e tente novamente.")
            print("!" * 45)
            continue

        print("\nOk! Balanço validado! Pode prosseguir.")      
        return ativo_circulante, ativo_nao_circ, estoques, passivo_circulante, passivo_nao_circ, passivo_total, patrimonio_liquido, receita_liquida, lucro_liquido
    
def boas_vindas():
    print("\nBem-vindo ao Dashboard Financeiro!")

    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            dados = coletar_dados()      # <- Mudei isso aqui para bater com o código do aluno 2.
            calcular_indicadores(dados)  # <- Mudei isso aqui para bater com o código do aluno 2.
        
        elif opcao == "2":
            print("\nAté mais! Encerrando o sistema...")
            break
        
        else:
            print("\nErro! Opção invalida! Tente novamente.")
