##Exercício 1: O Registro do Sistema (I/O e Tipagem)
##Crie um programa que simule o registro de um novo usuário, solicitando as seguintes informações:

##Nome do usuário (string).
##Ano de nascimento (inteiro).
##Altura em metros (float).
##O programa deve calcular a idade atual e exibir a mensagem:
##"Olá, [Nome]! Você tem [Idade] anos e sua altura é de [Altura]m. Registro concluído."

#Entrada
nome = str(input(print("Digite o Seu Nome:")))
anonasc = int(input(print("Digite Seu Ano de Nascimento")))
altura =float(input(print("Qual é Sua Altura")))
#Calculos
ano = 2026
idade = ano - anonasc
#Saída 
print("Olá,",nome,"! Você tem,",idade,"anos e sua altura é de",altura,"m.")
print("Registro concluído!")