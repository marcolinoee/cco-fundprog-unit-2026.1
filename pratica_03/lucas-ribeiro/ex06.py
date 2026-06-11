x = 10 # --> Escopo global

def teste():
    y = 5 # --> Escopo local
    return x + y

print(teste())

# Anotação
# x é um escopo global pois está fora da função, não podendo ser acessada de dentro da função.
# y é um escopo local pois está dentro da função, portanto, só existe dentro da mesma.
