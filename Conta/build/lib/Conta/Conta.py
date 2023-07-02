class Conta:
    contador_id = 0

    """Classe Conta
    Description: Classe que realiza a construção de uma conta bancária
    Atributos: 
        1. saldo: Valor presente na conta
        2. limite_saques: Limite total de saques que a conta pode realizar
        3. id: Identificador único da conta
        4. historico: Mantém o histórico da conta
    """

    def __init__(self, saldo=0, limite_saques=3):
        self.saldo = saldo
        self.limite_saques = limite_saques
        self.id = Conta.contador_id
        Conta.contador_id += 1
        self.historico = []

    def imprimir_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

    def imprimir_historico(self):
        historico_str = "Histórico de transações:\n"
        for transacao in self.historico:
            historico_str += f"{transacao}\n"
        return historico_str

    def sacar(self, valor):
        if self.saldo >= valor and self.limite_saques > 0:
            self.saldo -= valor
            self.limite_saques -= 1
            self.historico.append(f"Saque: - R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou limite de saques atingido.")

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito: + R$ {valor:.2f}")
