##Exercício 4: Verificador de Acesso (Lógica e Relacionais)
##Desenvolva um sistema de verificação que solicite a idade e os anos de experiência do usuário.

##Regra Importante: Não utilize if/else. O programa deve imprimir apenas True ou False para a condição de acesso.
#Regra Lógica: Acesso = ( Idade ≥ 18 ) AND ( Experiencia > 2 )

##Saída esperada: "Acesso Liberado: True".
#Entrada
idade = 0
experiencia = 0
acesso = False
#calculo
while acesso == False:
  idade = int(input("Qual é sua Idade?"))
  experiencia = int(input("Quantos Anos de Experência?"))
  acesso = (idade >= 18) and (experiencia >= 2)
  print("Acesso liberado", acesso)
#Saida
