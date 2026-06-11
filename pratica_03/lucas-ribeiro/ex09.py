#Explicando erro

# def dividir(a, b): 
    # return a / b

# print(dividir(10, 0)) --> não é possível dividir nenhum número por zero, logo, em python ocorre um erro.

# Correção

def dividir(a, b):
    if b == 0:
        return 'Não é possível dividir nenhum número por 0!'
    return a / b

print(dividir(10, 0))