##Desenvolva um script para calcular o valor de um projeto freelancer solicitando:

##O valor cobrado por hora.
##A estimativa de horas para conclusão.
##Exiba o valor bruto, o valor dos impostos (15%) e o valor líquido final.

##Fórmulas:
#ValorBruto=Horas×ValorHora
#Impostos=ValorBruto×0.15
#ValorLiquido=ValorBruto−Impostos

#Entrada
vhrscobra = float(input(print("Valor Cobrado por Hora:")))
hrsconc = float(input(print("Qual é a Estimativa de Horas para Conclusão:")))
#Calculo
bruto = hrsconc * vhrscobra
imposto = bruto * 0.15
vliquido = bruto - imposto

#Saída
print("Valor Bruto:",bruto,"","Impostos:",imposto,", Valor Líquido Final: ", vliquido)