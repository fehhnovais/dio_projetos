menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 5


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f} \n"
        else:
            print (" operacao falhou! o valor informado é invalido")

    elif opcao=="s":
        valor = float(input(" informe o valor do saque: "))
       
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
    
        excedeu_saque = numero_saque >= limite_saque
    
        if excedeu_saldo:
            print(" operacao falhou! voce nao tem saldo suficiente")

        elif excedeu_limite:
            print("operacao falhou! o valor do saque excede o limite.")

        elif excedeu_saque:
            print("operacao falhou! numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f" saque: R$ {valor: .2f}\n"
            numero_saque += 1
        
        else:
            print(" operacao falhou o valor informado é invalido")

    elif opcao == "e":
        print("\n===========extrato==========")
        print(" nao foram realizados movimentos." if not extrato else extrato)
        print (f"\n saldo: R${ saldo: .2f}")
        print("==============================")

    elif opcao =="q":
        break

    else:
        print ("operacao invalida, por favor selecione novamento a operacao desejada")





    


       
    




