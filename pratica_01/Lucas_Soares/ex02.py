valorhora=float(input('Qual valor da hora?'))
hora=float(input('Quantas horas serão?'))
valorbruto = valorhora * hora
imposto = valorbruto * 0.15
valorliquido = valorbruto - imposto

print('Este é o valor bruto',valorbruto,' esta é a quantia de imposto pago',imposto,' e este é o10 valor liquido',valorliquido,'')