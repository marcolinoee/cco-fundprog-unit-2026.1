x = 10 # Variável global

def teste():
    y = 5 # Variável local

# y = 5 se usar fora da função, dará erro, pois a variável y 
# é local e só existe dentro da função teste()

    return x + y

print(teste())

###############################################################

i = 3 # Variável global 

def teste2():
    o = 5 # Variável local

    return i * o

print(teste2())