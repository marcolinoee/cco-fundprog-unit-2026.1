idade = int(input("Insira sua idade: "))
exp = int(input("Insira sua experiência em anos: "))
acesso = (idade >= 18) and (exp >= 2)
print("Acesso liberado:", acesso)