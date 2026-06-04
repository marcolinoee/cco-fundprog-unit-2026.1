
while True:
    nota = int(input('Digite uma nota '))

    if nota < 0 or nota > 10:
        print('Voce digitou uma nota invalida')
        continue
    else:
        break
