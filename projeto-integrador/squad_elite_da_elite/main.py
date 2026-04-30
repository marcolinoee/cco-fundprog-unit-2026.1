from limpeza import limpeza_dos_dados
from classes import calcularAnalytics
from relatorios import gerar_grafico_vendas

def main():
    print("--- FASE 1: INGESTÃO (Digite os dados e aperte Enter) ---")
    print("Formato: DATA,PRODUTO,QUANTIDADE,VALOR,ESTADO")
    print("Digite 'FIM' para encerrar e gerar o gráfico.\n")

    linhas_brutas = []

    while True:
        entrada = input("Próxima linha: ")

        if entrada.upper() == 'FIM':
            break

        if entrada.strip() == "":
            continue

        linhas_brutas.append(entrada)

   
    linhas_processadas = limpeza_dos_dados(linhas_brutas) 
    vendas_estado = calcularAnalytics(linhas_processadas)
    gerar_grafico_vendas(vendas_estado)

if __name__ == "__main__":
    main()