print('Calcule o valor do seu trabalho freelancer repondendo as informações pedidas. ')

valor_hora = float(input('\nQual o valor da sua hora de trabalho?: '))
hora_trabalho = int(input('Quanto tempo você irá trabalhar?: '))

valor_bruto = (hora_trabalho * valor_hora)
imposto = valor_bruto * 0.15
valor_liq = valor_bruto - imposto

print(f'\nO valor bruto do seu trabalho é de {valor_bruto:.2f}R$')
print(f'O valor do imposto de 15% é de {imposto:.2f}R$')
print(f'\nO valor final a ser recebido é {valor_liq:.2f}R$')

