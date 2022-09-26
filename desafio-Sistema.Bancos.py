menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_saques = 3

while True:

    opcao = input(menu)

    if opcao  == "d":
        valor = float(input("Informe o valor do deposito:"))

        if valor > 0:
            saldo += valor 
            extrato += f"deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou!! O valor informado é invalido")
        

    elif opcao == "s":
       valor =  float(input("Informe o valor do saque:"))

       execedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saque = numero_saques >= Limite_saques

       if execedeu_saldo:
        print("Operação falhou !! O valor não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação falhou !! O valor de saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou !! Numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor 
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print ("Operação falhou !! O valor informado é invalido.")

    elif opcao == "e":
        print("\n==========Extrato==========")
        print("Não foram realizadas movimentaçoes" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        break

    else: 
        print("Operação invalida, por favor selelcione novamente a operação desejada.")




  