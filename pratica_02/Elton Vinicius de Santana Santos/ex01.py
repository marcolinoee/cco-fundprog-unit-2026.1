print("="*50)
print("Classificação de Número")
print("="*50)

Numero = int(input("Qual o numero: "))

if Numero == 0:
    print("Número Neutro")

elif Numero < 0:
    print("Número Negativo")

else:
    print("Número Positivo")