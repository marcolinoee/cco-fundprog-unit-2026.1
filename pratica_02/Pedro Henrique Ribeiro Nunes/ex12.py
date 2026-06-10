while True:
    valor = float(input('Digite o valor da compra: '))
    sn = str(input('Deseja continuar? Responda S para sim e N para não. ')).upper()
    if sn == 'S':
        continue
    elif sn == 'N':
        break
    