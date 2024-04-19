menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor, saldo_atual):
    global extrato
    extrato_atual = ""
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo_atual += valor
        extrato_atual += f"Depósito: R$ {valor:.2f}\n"
    return extrato_atual, saldo_atual

def sacar(valor, saldo_atual, num_saques):
    global extrato
    extrato_atual = extrato
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo_atual:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite_saque:
        print(f"Operação falhou! O valor do saque excede o limite de {limite_saque}.")
    elif num_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo_atual -= valor
        extrato_atual += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
    return extrato_atual, saldo_atual, num_saques

def exibir_extrato(extrato_atual, saldo_atual):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_atual else extrato_atual)
    print(f"\nSaldo: R$ {saldo_atual:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        extrato, saldo = depositar(valor, saldo)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        extrato, saldo, numero_saques = sacar(valor, saldo, numero_saques)

    elif opcao == "e":
        exibir_extrato(extrato, saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")