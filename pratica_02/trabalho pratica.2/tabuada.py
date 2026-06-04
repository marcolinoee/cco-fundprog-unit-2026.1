import os 
os.system("cls")

numero = int(input("digite um número para ver a tabuada: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")