saldo = 0
limite_saque = 500
extrato = ""
LIMITE_SAQUES = 5
numero_saques = 0  # Movido para fora da função saque

def depositar(saldo, extrato):
    valor = float(input("Digite o valor que deseja depositar: "))
    if valor < 0:
        print("Não é permitido o depósito de valores negativos")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def saque(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saque
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("A operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("A operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("A operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! O valor informado é inválido')
    
    return saldo, extrato, numero_saques



menu = """

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato


=> """

while True:
    opcao = input(menu)
    if opcao == '1':
        saldo, extrato = depositar(saldo, extrato)
        print(f"Depósito feito com sucesso! Saldo atual: {saldo}")

    elif opcao == "2":
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques)
        print(f"Saque feito com sucesso! Saldo atual: {saldo}")

    elif opcao == "3":
        print("\n ================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")

