import os
# ============================================
# SISTEMA ABC - PRIMEIRA ENTREGA
# ============================================
 
def linha():
    print("*" * 30)
def nome_produto(nome):
    print(f'\n{nome}\n')
def limpar_terminal():
    os.system('cls')
# CADASTRO DE PRODUTOS

linha()
print('=== CADASTRE SEUS PRODUTOS ===')
linha()

# CADASTRO PRODUTO 1
nome_produto('CADASTRO DO PRIMEIRO PRODUTO')

nome_produto_1 = input(f"Digite o nome do primeiro produto --> ")
quantidade_produto_1 = float(input(f"Digite a quantidade de {nome_produto_1}s --> "))
custo_direto_produto_1 = float(input(f"Digite o custo direto de {nome_produto_1}s --> "))

# CADASTRO PRODUTO 2
nome_produto('CADASTRO DO SEGUNDO PRODUTO')

nome_produto_2 = input(f"Digite o nome do segundo produto --> ")
quantidade_produto_2 = float(input(f"Digite a quantidade de {nome_produto_2}s --> "))
custo_direto_produto_2 = float(input(f"Digite o custo direto de {nome_produto_2}s --> "))

# CADASTRO DE ATIVIDADES

limpar_terminal()

print('\n')
linha()
print('== CADASTRE SUAS ATIVIDADES ==')
linha()

# CADASTRO ATIVIDADE 1
nome_produto("CADASTRO DA PRIMEIRA ATIVIDADE")

nome_atividade_1 = input(f'Digite o nome da primeira atividade --> ')
custo_atividade_1 = float(input(f'Digite o custo de {nome_atividade_1} --> '))

# CADASTRO ATIVIDADE 2
nome_produto("CADASTRO DA SEGUNDA ATIVIDADE")

nome_atividade_2 = input(f'Digite o nome da segunda atividade --> ')
custo_atividade_2 = float(input(f'Digite o custo de {nome_atividade_2} --> '))

# CADASTRO CONSUMO DAS ATIVIDADES

limpar_terminal()

print('\n')
linha()
print('=== CONSUMO DAS ATIVIDADES ===')
linha()

# CONSUMO PRODUTO 1
print(f'\n{nome_produto_1}: ')
consumo_do_prod1_atividade1 = float(input(f'Consumo de {nome_atividade_1} --> '))
consumo_do_prod1_atividade2 = float(input(f'Consumo de {nome_atividade_2} --> '))

# CONSUMO PRODUTO 2
print(f'\n{nome_produto_2}: ')
consumo_do_prod2_atividade1 = float(input(f'Consumo de {nome_atividade_1} --> '))
consumo_do_prod2_atividade2 = float(input(f'Consumo de {nome_atividade_2} --> '))


# ============================================
# SISTEMA ABC - CÁLCULOS
# ============================================

# CÁLCULOS DAS TAXAS

total_atividade1 = consumo_do_prod1_atividade1 + consumo_do_prod2_atividade1
total_atividade2 = consumo_do_prod1_atividade2 + consumo_do_prod2_atividade2

taxa1 = custo_atividade_1 / total_atividade1
taxa2 = custo_atividade_2 / total_atividade2

# CUSTOS INDIRETOS 

# Primeiro produto:
custo_indireto1 = (consumo_do_prod1_atividade1 * taxa1) + (consumo_do_prod1_atividade2 * taxa2)
# Segundo produto:
custo_indireto2 = (consumo_do_prod2_atividade1 * taxa1) + (consumo_do_prod2_atividade2 * taxa2)

# CUSTO TOTAL 

custo_total1 = custo_direto_produto_1 + custo_indireto1
custo_total2 = custo_direto_produto_2 + custo_indireto2

# CUSTO UNITÁRIO 

custo_unitario1 = custo_total1 / quantidade_produto_1 
custo_unitario2 = custo_total2 / quantidade_produto_2

limpar_terminal()

linha()
print('=== RESULTADO FINAL ===')
linha()

print(f'{nome_produto_1}:')
print(f'O custo unitário(por unidade): R${custo_unitario1}')
print(f'{nome_produto_2}:')
print(f'O custo unitário(por unidade): R${custo_unitario2}')