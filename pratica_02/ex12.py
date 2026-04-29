cont = 'S'
tcomp = 0.0

while cont.upper() == 'S':
    vcomp = float(input("Insira o valor da compra: R$ "))
    tcomp += vcomp
    cont = input("Deseja inserir outra continuar? (S/N) ")

print( "-" * 30 )
print("Total da compra: R$ " + str(tcomp))
print("Programa encerrado. Volte sempre!")