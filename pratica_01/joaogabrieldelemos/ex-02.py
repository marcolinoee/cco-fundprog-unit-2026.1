valor_hora = float(input('Qual o valor da hora?'))
hora = float (input('Quantas horas são?'))
valorbruto = valor_hora * hora
imposto = valorbruto * 0.15
valor_liq = valorbruto - imposto
print ('Este é o valor bruto', valorbruto, 'está é a quantidade de imposto pago', imposto, 'e este é o valor líquido: ', valor_liq)
