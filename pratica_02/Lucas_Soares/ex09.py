while True:
    quanto_ganha = input('Digite qual seu salario ')

    try:
        quanto_ganha_float = float(quanto_ganha)
        
        if quanto_ganha_float <= 1500.00:
            aumento = quanto_ganha_float * 0.15
            novo_salario = quanto_ganha_float + aumento
            print(f'Este é seu novo salario R${novo_salario:.2f}')
            break

        elif quanto_ganha_float > 1500.01 or quanto_ganha_float < 3000.00:
            aumento = quanto_ganha_float * 0.10
            novo_salario = quanto_ganha_float + aumento
            print(f'Este é seu novo salario R${novo_salario:.2f}')
            break
        
        elif quanto_ganha_float > 3000.00:
            aumento = quanto_ganha_float * 0.05
            novo_salario = quanto_ganha_float + aumento
            print(f'Este é seu novo salario R${novo_salario:.2f}')
            break

       
    except:
        print('Digite um valor valido')
        