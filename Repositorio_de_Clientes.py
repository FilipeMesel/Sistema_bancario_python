# from Conta import Conta
# class RepositorioClientes:

#     """Classe RepositorioClientes
#         Description: Classe que representa uma coleção de clientes
#         Atributos: 
#                     1. clientes: Lista de clientes
#     """

#     def __init__(self):
#         self.clientes = []

#     def adicionar_cliente(self, cliente):
#         """Função para adicionar cliente ao repositório

#         Args:
#             cliente (cliente): Objeto da classe Cliente
#         """
#         self.clientes.append(cliente)
#         print(f"Cliente {cliente.nome} adicionado com sucesso!")

#     def excluir_cliente(self, cliente_nome):
#         """Função Excluir Cliente

#         Args:
#             cliente (Cliente): Objeto da classe Cliente
#         """
#         for cliente in self.clientes:
#             if cliente.nome == cliente_nome:
#                 self.clientes.remove(cliente)
#                 print(f"Cliente {cliente.nome} removido com sucesso!")
#                 return

#         print(f"Cliente com Nome {cliente_nome} não encontrado!")

#     def listar_clientes(self):
#         """Função Listar Cliente

#         Returns:
#             clientes: Lista de objetos da classe Cliente
#         """
#         return self.clientes

#     def buscar_cliente_nome(self, cliente_nome):
#         """Função Buscar Cliente por ID

#         Args:
#             cliente_nome (text): ID do cliente a ser buscado
#         """
#         for cliente in self.clientes:
#             if cliente.nome == cliente_nome:
#                 return cliente

#         print(f"Cliente com Nome {cliente_nome} não encontrado!")
#         return None

#     def adicionar_conta(self, cliente_nome, saldo, limite_saques):
#         """Função Adicionar Conta ao Cliente

#         Args:
#             cliente_nome (text): Nome do cliente
#             saldo (float): Saldo da conta
#             limite_saques (int): Limite de saques da conta
#             conta_id (text): ID da conta
#         """
#         for cliente in self.clientes:
#             if cliente.nome == cliente_nome:
#                 conta = Conta(saldo, limite_saques)
#                 cliente.adicionar_conta(conta)
#                 print(f"Conta adicionada ao cliente {cliente.nome} com sucesso!")
#                 return

#         print(f"Cliente com Nome {cliente_nome} não encontrado!")

#     def listar_contas(self, cliente_nome):
#         """Função Listar Contas

#         Args:
#             cliente_nome (text): Nome do cliente
#         """
#         for cliente in self.clientes:
#             if cliente.nome == cliente_nome:
#                 return cliente.contas

#         print(f"Cliente com Nome {cliente_nome} não encontrado!")
#         return None

from datetime import datetime as dt
from Conta.Conta import Conta

class RepositorioClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso!")
    
    def listar_clientes(self):
        """Retorna a lista de clientes"""
        return self.clientes

    def excluir_cliente(self, cliente_id):
        cliente = self.buscar_cliente_id(cliente_id)
        if cliente:
            if cliente.contas:
                print(f"Não é possível excluir o cliente {cliente.nome} porque ele possui contas.")
            else:
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nome} removido com sucesso!")
        else:
            print(f"Cliente com ID {cliente_id} não encontrado!")

    def listar_contas_cliente(self, cliente_id):
        cliente = self.buscar_cliente_id(cliente_id)
        if cliente:
            return cliente.listar_contas()
        else:
            print(f"Cliente com ID {cliente_id} não encontrado!")
            return None

    def criar_conta(self, cliente_id, saldo=0, limite_saques=3):
        cliente = self.buscar_cliente_id(cliente_id)
        if cliente:
            conta = Conta(saldo, limite_saques)
            cliente.adicionar_conta(conta)
            print(f"Conta criada para o cliente {cliente.nome} com sucesso!")
        else:
            print(f"Cliente com ID {cliente_id} não encontrado!")

    def transacionar_conta(self, cliente_id, conta_id, valor):
        cliente = self.buscar_cliente_id(cliente_id)
        if cliente:
            conta = self.buscar_conta_cliente(cliente, conta_id)
            if conta:
                if valor > 0:
                    conta.depositar(valor)
                    print(f"Transação realizada com sucesso na conta {conta.id} do cliente {cliente.nome}.")
                elif valor < 0:
                    conta.sacar(abs(valor))
                    print(f"Transação realizada com sucesso na conta {conta.id} do cliente {cliente.nome}.")
                else:
                    print("O valor da transação precisa ser diferente de zero.")
            else:
                print(f"Conta com ID {conta_id} não encontrada para o cliente {cliente.nome}!")
        else:
            print(f"Cliente com ID {cliente_id} não encontrado!")

    def apagar_conta(self, cliente_id, conta_id):
        cliente = self.buscar_cliente_id(cliente_id)
        if cliente:
            conta = self.buscar_conta_cliente(cliente, conta_id)
            if conta:
                cliente.remover_conta(conta.id)
                print(f"Conta {conta.id} do cliente {cliente.nome} removida com sucesso!")
            else:
                print(f"Conta com ID {conta_id} não encontrada para o cliente {cliente.nome}!")
        else:
            print(f"Cliente com ID {cliente_id} não encontrado!")

    def buscar_cliente_id(self, cliente_id):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        print(f"Cliente com ID {cliente_id} não encontrado!")
        return None

    def buscar_conta_cliente(self, cliente, conta_id):
        for conta in cliente.contas:
            if conta.id == conta_id:
                return conta
        return None
