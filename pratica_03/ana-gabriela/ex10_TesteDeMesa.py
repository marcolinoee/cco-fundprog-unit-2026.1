def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

print(calcular_total(50, 2)) 
print(calcular_total(100, 3))
print(calcular_total(0, 5)) 
print(calcular_total(1000000, 100))