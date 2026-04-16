##Exercício 3: Divisão Justa (Divisão Inteira e Módulo)
##Crie um programa para dividir fatias de pizza entre uma equipe, perguntando:

##O número total de fatias.
##O número de programadores na equipe.
##Calcule e imprima quantas fatias inteiras cada um comerá e o resto que sobrará na caixa.

#Fórmulas:
##FatiasPorPessoa=TotalFatias/Programadores
##Sobra=TotalFatias
print("Divisor de Fatias")
ttfatias=int(input(print("Qual é o número total de fatias?")))
pessoa=int(input(print("Qual é o número de pessoas na equipe?")))
fppessoa = ttfatias / pessoa
sobra = ttfatias

print("Cada Pessoa Terá:",fppessoa,"Sobrando:",sobra)