idade = int(input("Digite a sua idade: "))
experiencia_anos = int(input("Digite a sua experiência em (anos): "))

acesso = (idade >= 18) and (experiencia_anos >= 2)

print(f'Acesso liberado: {acesso}')