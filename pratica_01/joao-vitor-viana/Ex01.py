import os
nome = input('Qual é o seu nome? ')
ano_nasc = int(input('Qual foi o ano que você nasceu? '))
altura = float(input('Quantos metros você tem? '))
ano_atual = 2026

idade = ano_atual - ano_nasc

print(f'Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.')