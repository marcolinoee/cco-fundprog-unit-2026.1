idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite sua experiência em anos: "))

while idade < 18 and experiencia < 2:
    print("Acesso negado. Você deve ter pelo menos 18 anos e 2 anos de experiência.")
    acesso = False
    break
while idade >= 18 and experiencia >= 2:
    print("Acesso permitido. Bem-vindo!")
    acesso = True
    break
    