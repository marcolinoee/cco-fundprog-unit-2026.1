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
        passivo_circulante = ler_valor("Passivo Circulante: R$ ")
        passivo_nao_circ   = ler_valor("Passivo Não Circulante: R$ ")
        passivo_total      = passivo_circulante + passivo_nao_circ
        print(f"-> Passivo Total: R$ {passivo_total}")

        print("\nPATRIMÔNIO LÍQUIDO:")
        patrimonio_liquido = ler_valor("Patrimônio Líquido: R$ ")

        print("\nDRE:")
        receita_liquida = ler_valor("Receita Líquida: R$ ")
        lucro_liquido   = ler_valor("Lucro Líquido: R$ ")

        # Parte da validação de ouro:
        soma_passivo_pl = passivo_total + patrimonio_liquido

        if ativo_total != soma_passivo_pl:
            print("\n" + "!" * 45)
            print("ERRO FATAL: BALANÇO NÃO FECHA!")
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

# definicoes de indicadores financeiros - Rafael Varella

def liquidez_corrente(ativo_circulante, passivo_circulante):
    if passivo_circulante == 0:
        return None
    return ativo_circulante / passivo_circulante


def margem_liquida(lucro_liquido, receita_liquida):
    if receita_liquida == 0:
        return None
    return lucro_liquido / receita_liquida


def roe(lucro_liquido, patrimonio_liquido):
    if patrimonio_liquido == 0:
        return None
    return lucro_liquido / patrimonio_liquido


def endividamento(passivo_total, patrimonio_liquido):
    total = passivo_total + patrimonio_liquido
    if total == 0:
        return None
    return passivo_total / total


def liquidez_seca(ativo_circulante, estoques, passivo_circulante):
    if passivo_circulante == 0:
        return None
    return (ativo_circulante - estoques) / passivo_circulante

def exibir_resultados(resultados):
    """Exibe os indicadores financeiros de forma formatada"""
    print("\n" + "=" * 45)
    print("INDICADORES FINANCEIROS - RESULTADOS")
    print("=" * 45)
    for chave, valor in resultados.items():
        if valor is not None:
            print(f"{chave.replace('_', ' ').title()}: {valor:.4f}")
        else:
            print(f"{chave.replace('_', ' ').title()}: N/A")
    print("=" * 45 + "\n")


# parte do motor analitico - Rafael Varella
def calcular_indicadores(dados):
    (
        ativo_circulante,
        estoques,
        ativo_nao_circ,
        passivo_circulante,
        passivo_nao_circ,
        patrimonio_liquido,
        receita_liquida,
        lucro_liquido,
        passivo_total
    ) = dados

    resultados = {}

    resultados["liquidez_corrente"] = liquidez_corrente(
        ativo_circulante,
        passivo_circulante
    )

    resultados["liquidez_seca"] = liquidez_seca(
        ativo_circulante,
        estoques,
        passivo_circulante
    )

    resultados["margem_liquida"] = margem_liquida(
        lucro_liquido,
        receita_liquida
    )

    resultados["roe"] = roe(
        lucro_liquido,
        patrimonio_liquido
    )

    resultados["endividamento"] = endividamento(
        passivo_total,
        patrimonio_liquido
    )

    exibir_resultados(resultados)
    return resultados
  
boas_vindas()
