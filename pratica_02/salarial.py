sal= float(input("Digite o seu salário: "))
if sal <= 1500:
    print("Você tem direito a um aumento de 15%")
    print(f"Seu novo salário é: {sal * 1.15}")
elif sal > 1501 and sal <= 3000:
    print("Você tem direito a um aumento de 10%")
    print(f"Seu novo salário é: {sal * 1.1}")
else:
    print("Você tem direito a um aumento de 5%")
    print(f"Seu novo salário é: {sal * 1.05:;.2f}")
