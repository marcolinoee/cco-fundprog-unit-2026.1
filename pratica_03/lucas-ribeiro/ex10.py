def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

print(calcular_total(6, 40)) # --> Caso normal 1
print(calcular_total(61, 2)) # --> Caso normal 2
print(calcular_total(1, 1)) # --> Caso limitrofe
print(calcular_total(9, -7)) # --> Caso extremo