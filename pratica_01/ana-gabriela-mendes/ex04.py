Idade = int(input("Digite sua idade: "))
Experiencia = float(input("Digite sua experiência em anos: "))

while True:
    acesso = (Idade >= 18) and (Experiencia >= 2)
    if acesso:
        print("Acesso permitido.")
        break
    else:
        print("Acesso negado.")
        break
