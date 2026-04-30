print("="*50)
print("sistema de verificação que solicite a **idade** e os **anos de experiência** do usuário.")
print("="*50)

Idade = int(input("Qual Sua Idade: "))
Anos_Experiencia = int(input("Quantos Anos de Experiencia: "))

Acesso = (Idade >= 18) and (Anos_Experiencia > 2)

print("="*50)
print(f"Acesso Liberado: {Acesso}")
print("="*50)