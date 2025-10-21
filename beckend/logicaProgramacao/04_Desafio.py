saldo = 0
def menu(saldo):
    print("Deposito - 1")
    print("Saque - 2")
    print("Saldo - 3")
    print("Sair - 4")
    opcao = int(input("Escolha uma Opção: "))

    if opcao == 1:
        deposito(saldo)
    elif opcao == 2:
        saque(saldo)
    elif opcao == 3:
        mostrar_saldo(saldo)
    elif opcao == 4:
        print("Saindo...")
    else:
        print("Opção inválida!")


def deposito(saldo):
    valor1 = float(input("Digite o valor para depositar: "))
    saldo += valor1
    print("Depósito de R$", valor1, "realizado com sucesso!")


def saque(saldo):
    valor2 = float(input("Digite o valor para Sacar: "))
    if valor2 > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor2
        print("Saque de R$", valor2, "realizado com sucesso!")


def mostrar_saldo(saldo):
    print("Seu saldo é: R$", saldo)


saldo = menu(saldo)