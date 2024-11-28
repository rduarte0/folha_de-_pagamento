import os
os. system ("cls || clear")


# Função para calcular o INSS
def calcular_inss(salario_base):
    if salario_base <= 1100.00:
        inss = salario_base * 0.075
    elif salario_base <= 2203.48:
        inss = salario_base * 0.09
    elif salario_base <= 3305.22:
        inss = salario_base * 0.12
    elif salario_base <= 6433.57:
        inss = salario_base * 0.14
    else:
        inss = 854.36  # Valor máximo
    return inss

# Função para calcular o IRRF
def calcular_irrf(salario_base, dependentes):
    deducao_dependente = dependentes * 189.59
    base_irrf = salario_base - calcular_inss(salario_base) - deducao_dependente

    if base_irrf <= 2259.20:
        irrf = 0
    elif base_irrf <= 2826.65:
        irrf = base_irrf * 0.075 - 171.97
    elif base_irrf <= 3751.05:
        irrf = base_irrf * 0.15 - 354.80
    elif base_irrf <= 4664.68:
        irrf = base_irrf * 0.225 - 636.13
    else:
        irrf = base_irrf * 0.275 - 869.36
    return max(irrf, 0)


def folha_pagamento():
    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha: ")  # Não estamos verificando a senha por questões de simplicidade
    salario_base = float(input("Digite o salário base do funcionário (R$): "))
   
    # Perguntando sobre o vale transporte
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
    if vale_transporte == 's':
        vt = salario_base * 0.06
    else:
        vt = 0

    # Perguntando o valor do vale refeição
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))
    vr = vale_refeicao * 0.20  # 20% de desconto no vale refeição

    # Desconto do plano de saúde
    plano_saude = 150.00  # Um dependente

    # Cálculo dos descontos
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes=1)
   
    # Salário líquido
    descontos = inss + irrf + vt + vr + plano_saude
    salario_liquido = salario_base - descontos

    # Exibindo dados
    print(f"\nMatrícula: {matricula}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")


folha_pagamento()