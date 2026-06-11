import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_menu():
    print("="*44)
    print("[1] Nova simulação")
    print("[2] Sair do programa")
    print('(Não escreva por extenso)')
    print("="*44)

    escolha = input("Digite sua escolha: ")
    while True:
        if escolha == '1':
            break
        elif escolha == '2':
            print('Encerrando Programa.....')
            exit()
        while escolha != '1' and escolha != '2' or escolha == '':
                limpa()
                print('Escolha um valor válido (1 ou 2) e não escreva por extenso: ')
                escolha = input('Digite novamente: ')

class MotorLucroReal:
    def __init__(self, faturamento, folha_de_pagamento, custos_operacionais):
        self.faturamento         = faturamento
        self.folha_de_pagamento  = folha_de_pagamento
        self.custos_operacionais = custos_operacionais

    def calcular_real(self):
        lucro  = self.faturamento - self.custos_operacionais
        irpj   = lucro * 0.15
        csll   = lucro * 0.09
        pis    = self.faturamento * 0.0165
        cofins = self.faturamento * 0.076
        imposto = irpj + csll + pis + cofins

        print("--- Lucro Real ---")
        print(f"Total imposto: \033[1;31mR$ {imposto:,.2f}\033[m\n")

        return imposto



def motor_simples_nacional(faturamento: float, ramo: str) -> float | None:

    tabelas = {
        "Comércio":   [(180000, 0.04), (360000, 0.073), (720000, 0.095), (1800000, 0.107), (float("inf"), 0.143)],
        "Serviços":   [(180000, 0.06), (360000, 0.112), (720000, 0.135), (1800000, 0.16),  (float("inf"), 0.21)],
        "Indústrias": [(180000, 0.045),(360000, 0.078), (720000, 0.10),  (1800000, 0.113), (float("inf"), 0.147)]
    }

    if ramo not in tabelas:
        return None

    for faixa, aliquota in tabelas[ramo]:
        if faturamento <= faixa:
            break

    imposto = faturamento * aliquota
    print("--- Simples Nacional ---")
    print(f"Total imposto: \033[1;31mR$ {imposto:,.2f}\033[m\n")
    return imposto

class motor_presumido:
    def __init__(self, faturamento, ramo):
        self.faturamento = faturamento
        self.ramo        = ramo
        self.imposto     = None

    def calcular_imposto(self):
        if self.ramo == "Comércio":
            base = self.faturamento * 0.08
        elif self.ramo == "Serviços":
            base = self.faturamento * 0.32
        elif self.ramo == "Indústrias":
            base = self.faturamento * 0.08
        else:
            return None

        irpj   = base * 0.15
        csll   = base * 0.09
        pis    = self.faturamento * 0.0065
        cofins = self.faturamento * 0.03

        self.imposto = irpj + csll + pis + cofins
        print("--- Lucro Presumido ---")
        print(f"Total imposto: \033[1;31mR$ {self.imposto:,.2f}\033[m\n")
        return self.imposto


def maior_menor(simples, presumido, real):
    regimes = {
        'Simples Nacional': simples,
        'Lucro Presumido':  presumido,
        'Lucro Real':       real
    }

    
    menos = min(regimes.values())
    mais  = max(regimes.values())

    
    for nome, valor in regimes.items():
        if valor == menos:
            regime_menor = nome
        if valor == mais:
            regime_maior = nome

    return {
        'regime menor': regime_menor,
        'regime maior': regime_maior,
        'barato':       menos,
        'caro':         mais
    }

def relatorio(comparacao):
    if comparacao['regime maior'] != comparacao['regime menor']:
        print(f'{comparacao["regime menor"]} é a opção mais barata. Economia de:\033[1;32m R$ {comparacao["caro"] - comparacao["barato"]:,.2f} \033[m')
    else:
        print('Os impostos possuem o mesmo custo.')
