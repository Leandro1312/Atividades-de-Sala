class ContaBancaria:
    def __init__(self, titular, saldo_inicial, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    def transferir(self, valor, conta_destino):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                conta_destino.depositar(valor)
                print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso!")
            else:
                print("Saldo insuficiente para a transferência.")
        else:
            print("O valor da transferência deve ser positivo.")
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
conta1 = ContaBancaria("leo", 1000.00, "12345-6", "Corrente")
conta2 = ContaBancaria("leandro", 500.00, "65432-1", "Poupança")
conta1.verificar_saldo()  
conta1.depositar(200.00)  
conta1.sacar(50.00)  
conta1.transferir(100.00, conta2)  
conta2.verificar_saldo() 