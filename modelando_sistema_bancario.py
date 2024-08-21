from abc import ABC, abstractclassmethod,abstractproperty
from datetime import datetime
import textwrap

class cliente:
    def __init__(self, endereco):
        self.endereco= endereco
        self.contas= []

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class pessoa_fisica(cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome=nome
        self.data_nascimento= data_nascimento
        self.cpf= cpf

class conta:
    def __init__(self, numero, cliente):
        self._saldo=0
        self._numero =numero
        self._agencia= "0001"
        self._cliente= cliente
        self._historico=historico()

abstractclassmethod
def nova_conta(cls,cliente,numero):
    return cls(numero, cliente)

abstractproperty
def saldo(self):
    return self._saldo

abstractproperty
def numero(self):
    return self._numero

abstractproperty
def agencia(self):
    return self._agencia

abstractproperty
def cliente(self):
    return self._cliente

abstractproperty
def historico(self):
    return self._historico

def sacar( self,valor):
    saldo=self.saldo
    excedeu_saldo=valor > saldo

    if excedeu_saldo:
        print (" \n@@@ opercacao falhou! Voce nao tem saldo suficiente. @@@")
    
    elif valor>0:
        self._saldo -= valor
        print (" \n@@@ saque realizado com sucesso! @@@")
        return True
    
    else:
        print(" \n@@@ operacao falhou! o valor informado é invalido. @@@")
        return False
    
def depositar(self, valor):
    if valor>0:
        self._saldo+= valor
        print(" \n@@@ deposito realizado com sucesso!  @@@")

    else:
        print(" \n@@@ operacao falhou! o valor informado é invalido. @@@")

    return True

class conta_corrente(conta):

    def __init__(self, numero, cliente, limite =500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite =limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saque =len( [transacao for transacao in self.historico.transacao
         if transacao["tipo"] ==saque.__name__] )
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saque > self.limite_saque

        if excedeu_limite:
            print (" \n@@@ operacao falhou! o valor de saque excedeu o limite. @@@")

        elif excedeu_saque:
           print (" \n@@@ operacao falhou! numero maximo de saques excedido. @@@")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
        agencia:\t{self.agencia}
        c/c:\t\t {self.numero}
        titular:\t{self.cliente.none}
        """
        
class historico:
    def __int__(self):
        self_transacoes=[]

    abstractproperty
    def transacoes(self):
        return  self._transacoes
    
    def adicionar_transacoes(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao._class_._name_,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%y %h:%m: %s"),
            }
        )

class transacao(ABC):
    abstractproperty
    def valor(self):
        pass

    abstractclassmethod
    def registrar(self,conta):
        pass


class saque(transacao):
    def __init__(self, valor):
     self._valor = valor

    abstractproperty
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao =conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transascao(self)
    

class deposito(transacao):

    def __init__(self, valor):
        super._valor=valor

    abstractproperty
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao=conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


    def menu():
        menu = """\n
        ============== menu =============
        [d]\tdepositar
        [s]\tsacar
        [e]\textrato
        [nc]\tnova conta
        [lc]\tlistar contas
        [nu]\t novo usuario
        [q]\tsair

        """
        return input(textwrap.dedent(menu))
    

    def filtrar_cliente(cpf,clientes):
        clientes_filtrados=[cliente for cliente in clientes if cliente.cpf==cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    

    def recuperar_conta_cliente(cliente):
        if not cliente.conta:
            print("\n@@@ cliente nao possui conta! @@@")
            return cliente.contas1[0]
        
    
    def depositar(clientes):
        cpf= input("informe o cpf do cliente: ")
        cliente= filtrar_cliente (cpf, clientes)

        if not cliente:
            print("\n@@@ cliente nao encontrado! @@@")
            return
        
        valor= float (input("informe o valor do deposito: "))
        transacao= deposito(valor)

        conta= recuperar_conta_cliente (cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)

    
    def sacar (clientes):
        cpf= input(" informe o cpf do cliente: ")
        cliente= filtrar_cliente (cpf, clientes)

        if not cliente:
            print("\n@@@ cliente nao encontrado! @@@")
            return
        
        valor= float(input("informe o valor do saque: "))
        transacao=saque(valor)

        conta = recuperar_conta_cliente(cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)


    def exibir_extrato(clientes):
        cpf=input("informe o cpf do cliente: ")
        cliente = filtrar_cliente (cpf, clientes)

        if not cliente:
            print("\n@@@ cliente nao encontrado! @@@")
            return
        
        conta= recuperar_conta_cliente(cliente)

        if not conta:
            return
        
        print ("\n ========== extrato ==========")
        transancoes = conta.historico.transacoes

        extrato =""

        if not transacao:
            extrato="nao foram realizados movimentacoes. "

        else:
            for transacao in transancoes:
                extrato += f"\n{transacao['tipo']}:\n\tr${transacao['valor']:.2f}"

        print(extrato)
        print(f"\nsaldo:\n\tR${conta.saldo:.2f}")
        print("=========================================")

        #======================================================================

    def criar_conta(numero_conta,clientes,contas):
        cpf=input("informe o cpf do cliente: ")
        cliente= filtrar_cliente(cpf, clientes)

        if not cliente:
            print("\n@@@ cliente nao encontrado, fluxo de criacao de conta encerrado! @@@")
            return
        
        conta = conta_corrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)

        print("\n@@@ conta criada com sucesso! @@@")

    
    def listar_contas(contas):

        for conta in contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
        


    def main():
        cliente=[]
        contas=[]

    while True:
        opcao= menu()
        
        if opcao =="d":
            depositar(cliente)

        elif opcao =="s":
            sacar(cliente)

        elif opcao =="e":
            exibir_extratro(cliente)

        elif opcao =="nu":
            criar_cliente(cliente)

        elif opcao =="nc":
            numero_conta= len(cliente)+1
            criar_conta(numero_conta, cliente, conta)

        elif opcao =="lc":
            listar_contas(conta)

        elif opcao=="q":
            break

        else:
            print("\n @@@ operacao invalida, por favor selecione novamente a operacao desejada. @@@")

    main()

        

    