import random


def teste():
    conta = ("Jason","1234")
    c = ContaC(conta)
    p = ContaP(conta)

    c.setaplicado(1000)
    c.setsaldo(1000)
    p.t()
    print(c.getsaldo())
def banco():
    conta = criarconta()
    c = ContaC(conta)
    p = ContaP(conta)
    print("Para efetuar a criação da conta, faça um deposito de ao menos R$: 10,00!")


    print("""
            ----------------------
            |     BLUE BANK      |
            ----------------------
            | 1 - DEPOSITAR      |
            | 2 - SAIR           |
            ----------------------
            """)

    op = int(input("Operação: "))
    if op == 1:
        stop = c.depositar()
        print("Sua conta foi criada com sucesso!!")
        while stop == True:

            print("""
                ----------------------
                |     BLUE BANK      |
                ----------------------
                | 1 - CONTA CORRENTE |
                | 2 - CONTA POUPANÇA |
                | 3 - SAIR           |
                ----------------------
                """)

            op = int(input("Operação: "))

            if op == 1:
                while True:
                    print("""
                        ----------------------
                        |     BLUE BANK      |
                        |   CONTA CORRENTE   |
                        ----------------------
                        | 1 - DEPOSITAR      |
                        | 2 - SACAR          |
                        | 3 - APLICAR        |
                        | 4 - VOLTAR         |
                        ----------------------
                        """)

                    op = int(input("Operação: "))
                    if op == 1:
                        stop = c.depositar()
                        break
                    elif op == 2:
                        stop = c.sacar()
                        break
                    elif op == 3:
                        stop = c.aplicar()
                        break
                    elif op == 4:
                        break
                    else:
                        print("Operação indisponivel!")
            elif op == 2:
                while True:
                    print("""
                    ----------------------
                    |     BLUE BANK      |
                    |   CONTA POUPANÇA   |
                    ----------------------
                    | 1 - RESGATAR       |
                    | 2 - EXTRATO        |
                    | 3 - VOLTAR         |
                    ----------------------
                    """)

                    op = int(input("Operação: "))
                    if op == 1:
                        saldos = p.resgatar(c.getsaldo(),c.getaplicado())
                        saldo = saldos[0]
                        aplicado = saldos[1]
                        if (type(saldo) != float):
                            stop = False
                        else:
                            c.setsaldo(saldo)
                            c.setaplicado(aplicado)
                            stop = True
                        break
                    elif op == 2:
                        stop = p.extrato(c.getsaldo(),c.getaplicado())
                        break
                    elif op == 3:
                        break
                    else:
                        print("Operação indisponivel!")
            elif op == 3:
                print("O programa foi encerrado")
                break
            else:
                print("Operação indisponivel!")

def criarconta():
    nome = input("Qual o nome do titular: ")
    senha = input("Digite sua senha: ")
    while len(senha) != 4:
        print("A senha deve possuir 4 digitos")
        senha = input("Digite sua senha: ")
    return nome,senha

class ContaC():
    def __init__(self,conta):
        self.__nome = conta[0]
        self.__nconta = random.randint(100,999)
        self.__senha = conta[1]
        self.__saldo = 0
        self.__aplicado = 0

    def setsaldo(self,novosaldo):
        self.__saldo = novosaldo
    def setaplicado(self,novosaldo):
        self.__aplicado = novosaldo
    def setsenha(self,novassenha):
        self.__senha = novassenha

    def getsaldo(self):
        return self.__saldo
    def getsenha(self):
        return self.__senha
    def getnome(self):
        return self.__nome
    def getnconta(self):
        return self.__nconta
    def getaplicado(self):
        return self.__aplicado

    def sacar(self):
        contador = 0
        veri = ""
        while self.getsenha() != veri:
            veri = input("Digite sua senha: ")
            contador += 1
            if self.getsenha() == veri:
                vs = float(input("Valor do saque: "))
                if vs > 0:
                    if vs < self.__saldo:
                        self.setsaldo(self.getsaldo() - vs)
                        print("Saque efetuado com sucesso")
                        return True
                    else:
                        print("Você não possui saldo o suficiente")
                else:
                    print("não é possivel sacar esse valor")
            if contador == 3:
                return False

    def depositar(self):
        contador = 0
        veri = ""
        while self.getsenha() != veri:
            veri = input("Digite sua senha: ")
            contador += 1
            if self.getsenha() == veri:
                vd = float(input("Valor do deposito:"))
                if vd > 0:
                    if vd<=10:
                        print("O deposito não foi efetuado, pois o valor minimo é de R$: 10,00")
                    else:
                        self.setsaldo(self.getsaldo() + vd)
                        print("O deposito foi efetuado com sucesso")
                        return True
                else:
                    print("Não é possivel depositar esse valor")
            if contador == 3:
                return False

    def aplicar(self):
        contador = 0
        veri = ""
        while self.getsenha() != veri:
            veri = input("Digite sua senha: ")
            contador += 1
            if self.getsenha() == veri:
                ap = float(input("Qual o valor a ser aplicado: "))
                if ap>0:
                    if ap<=self.__saldo:
                        self.__aplicado += ap
                        self.setsaldo(self.getsaldo()-ap)
                        print("O valor foi adicionado na sua conta poupança")
                    else:
                        print("Você não possui o valor para essa aplicação")
                    return True
                else:
                    print("Não é possivel aplicar esse valor")
            if contador == 3:
                return False

class ContaP(ContaC):
    def __init__(self,conta):
        super().__init__(conta)

    def resgatar(self,saldo,aplicado):
        contador = 0
        veri = ""
        while self.getsenha() != veri:
            veri = input("Digite sua senha: ")
            contador += 1
            if self.getsenha() == veri:
                r = float(input("Qual o valor do resgate: "))
                if r > 0:
                    if r < aplicado:
                        aplicado -= r
                        saldo += r
                    else:
                        print("Você não tem esse valor na sua poupança")
                else:
                    print("Não é possivel resgatar esse valor")
                return saldo,aplicado
            if contador == 3:
                return False

    def extrato(self,saldo,aplicado):
        contador = 0
        veri = ""
        while self.getsenha() != veri:
            veri = input("Digite sua senha: ")
            contador += 1
            if self.getsenha() == veri:
                print(f"""
                ----------------------
                |     BLUE BANK      |
                |  EXTRATO BANCARIO  |
                ----------------------
                 Nome: {self.getnome()}
                 Número da Conta: {self.getnconta()}
                 Conta Corrente
                 R$:  {saldo}
                 Conta Poupança
                 R$:  {aplicado}
                """)
                return True
            if contador == 3:
                return False
    def t(self):
        print(self.getnconta())
        print(self.getsaldo())
        print(self.getaplicado())
        print(self.getsenha())

banco()