# * Menor de idade: Menos de 18 anos.
# * Maior de idade: Entre 18 e 59 anos.
# * Idoso: 60 anos ou mais.

idade_pessoa = int(input('Digite sua idade: '))
if (idade_pessoa < 18):
    print('menor de idade')
elif(idade_pessoa < 60):
    print('maior de idade')
else:
    print('idoso')