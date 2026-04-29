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