import textwrap

def menu():
    menu = """\n
    [1]\tdepositar
    [2]\tsacar
    [3]\textrato
    [4]\tnova conta
    [5]\tlista contas
    [6]\tnovo usuario
    [0]\tsair
    """
    return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: \tR$ {valor:.2f}\n"
        print("\n== Deposito realizado com sucesso! ==")
    else:
        print("\n!!! Operação falhou! O valor informado é invalido. !!!")

    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saque,limite_saques):
    excedeu_saldo= valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque > limite_saques

    if excedeu_saldo:
        print("\n @@@ operacao falhou! voce nao tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n @@@ operacao falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saque:
        print("\n @@@ operacao falhou! Numero maximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"saque: \t\t R$ {valor: .2f} \n"
        numero_saque += 1
        print ("\n == saque realizado com sucesso!  ")

    else:
        print("\n @@@ operacao falhou! O valor informado é invalido. @@@")


    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n ===========EXTRATo===========")
    print(" nao foram realizados movimentacoes." if not extrato else extrato)
    print(f" \n saldo: |t|t R$ {saldo: .2f}")
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numero): ")
    usuario= filtar_usuario(cpf,usuarios)

    if usuario:
        print("\n @@@ ja existe usuario com esse cpf! @@@")

        return
    
    nome = input ("Informe o nome completo: ")
    data_nascimento= input(" Informe a data de nascimento (dd-mm-aaaa):  ")
    endereco = input(" Informe o endereço 9logradouro,nro-bairro-cidade/ sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })

    print("=== usuario criado com sucesso! ===")


def filtar_usuario(cpf,usuarios):
    usuarios_filtrados =[ usuario for usuario in usuario if usuario ["cpf"]]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta1(agencia,nuemro_conta, usuarios):
    cpf = input("Informe o cpf (somente numero): ")
    usuario= filtar_usuario(cpf,usuarios)

    if usuario:
        print("\n @@@ ja existe usuario com esse cpf! @@@")

        return{"agencia": agencia, "numero_conta": nuemro_conta, "usuario": usuario}
    
    print("\n @@@ usuario nao encontrado, fluxo de criacao de conta enceerrado! @@@")

    return None

def listar_contas(contas):
    for conta in contas:
        linha= f"""\
            agencia:\t{conta['agencia']}
            c/c: \t\t {conta['numero_conta']}
            titular:\t {conta["usuario"] ['none']}

            """
        print("=" * 100)
        print(textwrap.dedent(linha))

    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas)

        elif opcao == "5":
            numero_conta= len(contas)+1
            conta= criar_conta1( AGENCIA, numero_conta,usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("operacao invalida,por favor selecione novamente a operacao desejada.")
main()









