from limpeza import limpeza_dos_dados
from classes import Dataset  # Corrigido: Importando a classe correta
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

    # Processamento dos dados
    linhas_processadas = limpeza_dos_dados(linhas_brutas) 
    
    # Instanciando a classe e carregando os dados limpos
    sistema = Dataset()
    sistema.carregar_dados(linhas_processadas)
    
    # Executa o cálculo e armazena o retorno para o gráfico
    vendas_estado = sistema.calcular_analytics()
    
    # Gera o gráfico com os dados processados
    gerar_grafico_vendas(vendas_estado)

if __name__ == "__main__":
    main()