import pytest
from Repositorio_de_Clientes import RepositorioClientes
from Conta.Conta import Conta
from Cliente.Cliente import Cliente

# python -m pytest Testes_Repositorio_Clientes.py --html=report.html

@pytest.fixture
def repo_clientes():
    return RepositorioClientes()

def test_adicionar_cliente(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    assert len(repo_clientes.clientes) == 1

def test_excluir_cliente_sem_contas(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    repo_clientes.excluir_cliente(cliente.id)
    assert len(repo_clientes.clientes) == 0

def test_excluir_cliente_com_contas(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    conta = Conta(saldo=1000, limite_saques=3)
    cliente.adicionar_conta(conta)  # Adiciona a conta ao cliente
    conta = cliente.listar_contas()[0]  # Acessa a lista de contas do cliente
    repo_clientes.excluir_cliente(cliente.id)
    assert len(repo_clientes.clientes) == 1
    assert len(cliente.listar_contas()) == 1

def test_listar_contas_cliente(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    conta = Conta(saldo=1000, limite_saques=3)
    cliente.adicionar_conta(conta)  # Adiciona a conta ao cliente

    contas = repo_clientes.listar_contas_cliente(cliente.id)
    assert len(contas) == 1

def test_criar_conta(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    conta = Conta(saldo=1000, limite_saques=3)
    repo_clientes.criar_conta(cliente.id, conta.saldo, conta.limite_saques)
    contas = repo_clientes.listar_contas_cliente(cliente.id)
    for conta in contas:
        print(conta.saldo)
    assert len(contas) == 1

def test_transacionar_conta(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    repo_clientes.criar_conta(cliente.id)
    conta = repo_clientes.listar_contas_cliente(cliente.id)[0]
    repo_clientes.transacionar_conta(cliente.id, conta.id, 1000)
    assert conta.saldo == 1000
    repo_clientes.transacionar_conta(cliente.id, conta.id, -500)
    assert conta.saldo == 500

def test_apagar_conta(repo_clientes):
    cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                      "Assalariado", False, 5000, "Comprar uma casa")
    repo_clientes.adicionar_cliente(cliente)
    repo_clientes.criar_conta(cliente.id)
    conta = repo_clientes.listar_contas_cliente(cliente.id)[0]
    repo_clientes.apagar_conta(cliente.id, conta.id)
    assert len(repo_clientes.listar_contas_cliente(cliente.id)) == 0
