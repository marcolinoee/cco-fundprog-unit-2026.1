valores = [0 , 5, -3]

def lerValores(valores):
    for valor in valores:
        if valor < 0:
            print(f"O valor {valor} é negativo.")
        elif valor > 0:
            print(f"O valor {valor} é positivo.")
        else:
            print(f"O valor {valor} é zero.")

lerValores(valores)
        