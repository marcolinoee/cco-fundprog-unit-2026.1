# INGRESSO DE DADOS - JEAN SOARES

def exibir_menu():
    print("\n" + "=" * 45)
    print("DASHBOARD FINANCEIRO - SISTEMA CONTÁBIL")
    print("=" * 45)
    print("(1) Inserir dados de um ano")
    print("(2) Ver histórico da empresa")
    print("(3) Ver análise horizontal")
    print("(4) Sair")
    print("=" * 45)

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
        print(f"-> Ativo Total: R$ {ativo_total:,.2f}")

        print("\nPASSIVOS:")
        passivo_circulante = ler_valor("Passivo Circulante:     R$ ")
        passivo_nao_circ   = ler_valor("Passivo Não Circulante: R$ ")
        passivo_total      = passivo_circulante + passivo_nao_circ
        print(f"-> Passivo Total: R$ {passivo_total:,.2f}")

        print("\nPATRIMÔNIO LÍQUIDO:")
        patrimonio_liquido = ler_valor("Patrimônio Líquido: R$ ")

        print("\nDRE:")
        receita_liquida = ler_valor("Receita Líquida: R$ ")
        lucro_liquido   = ler_valor("Lucro Líquido: R$ ")

        soma_passivo_pl = passivo_total + patrimonio_liquido

        if ativo_total != soma_passivo_pl:
            print("\n" + "!" * 45)
            print("ERRO FATAL: Balanço não fecha!")
            print(f"Ativo Total:        R$ {ativo_total:,.2f}")
            print(f"Passivo Total + PL: R$ {soma_passivo_pl:,.2f}")
            print("Verifique os valores e tente novamente.")
            print("!" * 45)
            continue

        print("\nOk! Balanço validado! Pode prosseguir.")
        return (ativo_circulante, estoques, ativo_nao_circ,
                passivo_circulante, passivo_nao_circ, passivo_total,
                patrimonio_liquido, receita_liquida, lucro_liquido)


# MOTOR ANALÍTICO - RAFAEL VARELLA

def liquidez_corrente(ativo_circulante, passivo_circulante):
    if passivo_circulante == 0:
        return None
    return ativo_circulante / passivo_circulante

def liquidez_seca(ativo_circulante, estoques, passivo_circulante):
    if passivo_circulante == 0:
        return None
    return (ativo_circulante - estoques) / passivo_circulante

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

def exibir_resultados(resultados):
    print("\n" + "=" * 45)
    print("INDICADORES FINANCEIROS - RESULTADOS")
    print("=" * 45)
    for chave, valor in resultados.items():
        if valor is not None:
            print(f"{chave.replace('_', ' ').title()}: {valor:.4f}")
        else:
            print(f"{chave.replace('_', ' ').title()}: N/A")
    print("=" * 45)

def calcular_indicadores(dados):
    (ativo_circulante, estoques, ativo_nao_circ,
     passivo_circulante, passivo_nao_circ, passivo_total,
     patrimonio_liquido, receita_liquida, lucro_liquido) = dados

    resultados = {}
    resultados["liquidez_corrente"] = liquidez_corrente(ativo_circulante, passivo_circulante)
    resultados["liquidez_seca"]     = liquidez_seca(ativo_circulante, estoques, passivo_circulante)
    resultados["margem_liquida"]    = margem_liquida(lucro_liquido, receita_liquida)
    resultados["roe"]               = roe(lucro_liquido, patrimonio_liquido)
    resultados["endividamento"]     = endividamento(passivo_total, patrimonio_liquido)

    exibir_resultados(resultados)
    return resultados


# HISTÓRICO DA EMPRESA - ALUNO 3

historico = []

def salvar_ano(ano, dados, indicadores):
    registro = {
        "ano":                ano,
        "ativo_circulante":   dados[0],
        "estoques":           dados[1],
        "ativo_nao_circ":     dados[2],
        "passivo_circulante": dados[3],
        "passivo_nao_circ":   dados[4],
        "passivo_total":      dados[5],
        "patrimonio_liquido": dados[6],
        "receita_liquida":    dados[7],
        "lucro_liquido":      dados[8],
        "liquidez_corrente":  indicadores["liquidez_corrente"],
        "liquidez_seca":      indicadores["liquidez_seca"],
        "margem_liquida":     indicadores["margem_liquida"],
        "roe":                indicadores["roe"],
        "endividamento":      indicadores["endividamento"],
    }
    historico.append(registro)

def exibir_historico():
    if not historico:
        print("\nNenhum ano cadastrado ainda.")
        return
    print("\n" + "=" * 45)
    print("HISTÓRICO DE ANOS CADASTRADOS")
    print("=" * 45)
    for registro in historico:
        print(f"\n  Ano: {registro['ano']}")
        print(f"  Receita Líquida:    R$ {registro['receita_liquida']:,.2f}")
        print(f"  Lucro Líquido:      R$ {registro['lucro_liquido']:,.2f}")
        lc = registro['liquidez_corrente']
        ml = registro['margem_liquida']
        r  = registro['roe']
        e  = registro['endividamento']
        print(f"  Liquidez Corrente:  {lc:.4f}" if lc else "  Liquidez Corrente: N/A")
        print(f"  Margem Líquida:     {ml:.4f}" if ml else "  Margem Líquida: N/A")
        print(f"  ROE:                {r:.4f}"  if r  else "  ROE: N/A")
        print(f"  Endividamento:      {e:.4f}"  if e  else "  Endividamento: N/A")
        print("-" * 45)


# ANÁLISE HORIZONTAL - ALUNO 4

def calcular_variacao(valor_novo, valor_velho):
    if valor_velho == 0:
        return None
    return ((valor_novo / valor_velho) - 1) * 100

def etiqueta(variacao):
    if variacao is None:
        return "N/A"
    if variacao >= 0:
        return f"\033[92m[CRESCIMENTO] +{variacao:.2f}%\033[0m"
    else:
        return f"\033[91m[QUEDA] {variacao:.2f}%\033[0m"

def analise_horizontal():
    if len(historico) < 2:
        print("\nÉ necessário ter pelo menos 2 anos cadastrados para a análise horizontal.")
        return

    print("\n" + "=" * 45)
    print("ANÁLISE HORIZONTAL - EVOLUÇÃO DOS ANOS")
    print("=" * 45)

    for i in range(1, len(historico)):
        ano_velho = historico[i - 1]
        ano_novo  = historico[i]

        print(f"\n  Comparando {ano_velho['ano']} → {ano_novo['ano']}")
        print("  " + "-" * 41)

        campos = [
            ("Lucro Líquido",       "lucro_liquido"),
            ("Receita Líquida",     "receita_liquida"),
            ("Ativo Circulante",    "ativo_circulante"),
            ("Passivo Circulante",  "passivo_circulante"),
            ("Patrimônio Líquido",  "patrimonio_liquido"),
            ("Liquidez Corrente",   "liquidez_corrente"),
            ("Margem Líquida",      "margem_liquida"),
            ("ROE",                 "roe"),
            ("Endividamento",       "endividamento"),
        ]

        for nome, chave in campos:
            v_velho = ano_velho[chave]
            v_novo  = ano_novo[chave]
            if v_velho is None or v_novo is None:
                print(f"  {nome:<22} N/A")
                continue
            variacao = calcular_variacao(v_novo, v_velho)
            print(f"  {nome:<22} {etiqueta(variacao)}")

    print("\n" + "=" * 45)


# MENU PRINCIPAL

def boas_vindas():
    print("\nBem-vindo ao Dashboard Financeiro!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ano = input("\nAno de referência (ex: 2025): ").strip()
            dados = coletar_dados()
            indicadores = calcular_indicadores(dados)
            salvar_ano(ano, dados, indicadores)
            print(f"\nAno {ano} salvo no histórico!")

        elif opcao == "2":
            exibir_historico()

        elif opcao == "3":
            analise_horizontal()

        elif opcao == "4":
            print("\nAté mais! Encerrando o sistema...")
            break

        else:
            print("\nErro! Opção inválida! Tente novamente.")

boas_vindas()