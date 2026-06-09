print("Bem-vindo ao programa de calculo freelancer!")
ValorPorHora = float(input("Digite o valor cobrado por hora: "))
HorasParaConcluir = float(input("Digite a estimativa de horas para conclusão: "))

ValorBruto = ValorPorHora * HorasParaConcluir
Impostos = ValorBruto * 0.15
ValorLiquido = ValorBruto - Impostos
print(f"O valor bruto do projeto é: R$ {ValorBruto}, o valor dos impostos é: R$ {Impostos} e o valor líquido é: R$ {ValorLiquido}")
