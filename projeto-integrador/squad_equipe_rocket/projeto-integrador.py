# PROJETO 15 - DASHBOARD FINANCEIRO
# INGRESSO DE DADOS - JEAN SOARES
# Parte do menu interativo:
def exibir_menu():
    print("\n" + "=" * 45)
    print("DASHBOARD FINANCEIRO")
    print("=" * 45)
    print("(1) Inserir dados de um ano")
    print("(2) Ver histórico")
    print("(3) Análise horizontal")
    print("(4) Análise vertical")
    print("(5) Sair")
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
    

# Definicoes de indicadores financeiros - Rafael Varella

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


# Parte do motor analitico - Rafael Varella
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

# ALUNO 3 - JOÃO GABRIEL
historico = []

def salvar_ano(ano, dados, indicadores):
    registro = {
        "ano": ano,
        "receita_liquida": dados[7],
        "lucro_liquido": dados[8],
        "patrimonio_liquido": dados[6],
        "indicadores": indicadores
    }

    historico.append(registro)
    print(f"\nDados do ano {ano} salvos no histórico!")

def exibir_historico():
    if not historico:
        print("\nNenhum dado cadastrado.")
        return
    print("\n=== HISTÓRICO ===")
    for item in historico:
        print(f"Ano: {item['ano']} | Lucro: R$ {item['lucro_liquido']:.2f}")

# Análise Vertical e Horizontal - Victor Kenuy

def calcular_variacao(valor_novo, valor_antigo):
    if valor_antigo == 0:
        return None
    return ((valor_novo - valor_antigo) / valor_antigo) * 100


def etiqueta(variacao):
    if variacao is None:
        return "N/A"
    elif variacao > 0:
        return f"[SUBIU] +{variacao:.2f}%"
    elif variacao < 0:
        return f"[CAIU] {variacao:.2f}%"
    else:
        return "[ESTÁVEL]"


# Análise Horizontal

def analise_horizontal(historico):
    if len(historico) < 2:
        print("\n Precisa de pelo menos 2 anos cadastrados.")
        return

    print("\n" + "=" * 55)
    print(f"{'ANÁLISE HORIZONTAL':^55}")
    print("=" * 55)

    for i in range(1, len(historico)):
        antigo = historico[i - 1]
        novo = historico[i]

        print(f"\n {antigo['ano']} → {novo['ano']}")
        print("-" * 55)

        print(f"{'Conta':<30}{'Variação':>25}")
        print("-" * 55)

        campos = [
            ("Receita Líquida", "receita_liquida"),
            ("Lucro Líquido", "lucro_liquido"),
            ("Patrimônio Líquido", "patrimonio_liquido"),
        ]

        for nome, chave in campos:
            valor_antigo = antigo.get(chave)
            valor_novo = novo.get(chave)

            if valor_antigo is None or valor_novo is None:
                print(f"{nome:<30}{'N/A':>25}")
                continue

            variacao = calcular_variacao(valor_novo, valor_antigo)
            print(f"{nome:<30}{etiqueta(variacao):>25}")

        print("-" * 55)

    print("=" * 55)


# Análise Vertical

def analise_vertical(historico):
    if not historico:
        print("\n Nenhum dado cadastrado.")
        return

    print("\n" + "=" * 55)
    print(f"{'ANÁLISE VERTICAL':^55}")
    print("=" * 55)

    for ano in historico:
        print(f"\n Ano: {ano['ano']}")
        print("-" * 55)

        print(f"{'Conta':<30}{'Percentual':>25}")
        print("-" * 55)

        receita = ano.get("receita_liquida")
        lucro = ano.get("lucro_liquido")

        if receita is None or receita == 0:
            print("Receita inválida.")
            continue

        percentual_lucro = (lucro / receita) * 100 if lucro is not None else None

        print(f"{'Receita Líquida':<30}{'100%':>25}")

        if percentual_lucro is not None:
            print(f"{'Lucro Líquido':<30}{percentual_lucro:.2f}%")
        else:
            print(f"{'Lucro Líquido':<30}{'N/A':>25}")

        print("-" * 55)

    print("=" * 55)


# MENU PRINCIPAL
def boas_vindas():
    print("\nBem-vindo ao Dashboard Financeiro!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ano = input("Ano de referência: ")
            dados = coletar_dados()
            indicadores = calcular_indicadores(dados)
            salvar_ano(ano, dados, indicadores)

        elif opcao == "2":
            exibir_historico()

        elif opcao == "3":
            analise_horizontal(historico)

        elif opcao == "4":
            analise_vertical(historico)

        elif opcao == "5":
            print(" Até mais! Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")



boas_vindas()
=======
>>>>>>> dbe447cb3e83227d5411aef6e86fbf5d0bc291d7
