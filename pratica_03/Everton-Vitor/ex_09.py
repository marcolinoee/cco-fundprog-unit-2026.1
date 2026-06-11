def dividir(a, b):
    return a / b

print(dividir(10, 0)) # Isso causará um erro de divisão por zero

# o erro que esta acontecendo é o ZeroDivisionError, que ocorre quando tentamos dividir um número por zero.
# para corrigir isso, podemos adicionar uma verificação para garantir que o divisor não seja zero antes de realizar a divisão. 
# aogra assim esta corrigida a função 😊:

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

print(dividir(10, 0)) # Isso causará um erro de divisão por zero
print(dividir(10, 2)) # Isso funcionará normalmente