num1=input(float("digite um numero: "))
num2=input(float("digite sua outra nota: "))
num3=input(float("digite sua ultima nota: "))

resultado=(num1 + num2 + num3)/3

if (resultado>=7):
    print("APROVADO")
else:
    print("REPROVADO")

print(f"o resultado da sua media é: {resultado:.2f}")