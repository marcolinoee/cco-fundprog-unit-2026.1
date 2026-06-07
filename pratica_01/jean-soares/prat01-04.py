# Verificador de acesso (True ou False) - Python

idade = int(input("Digite a sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

acesso = (idade >= 18 and idade < 120) and (experiencia > 2)

print(f"Acesso liberado: {acesso}")