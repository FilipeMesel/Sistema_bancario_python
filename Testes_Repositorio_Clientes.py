# python -m pytest Testes_Repositorio_Clientes.py --html=report.html

from datetime import datetime as dt
from DataBase import DataBase, Cliente, Conta

def test_data_base_add_client():
    DataBase.data_base_init()  # Inicializa a base de dados
    nome = "John Doe"
    idade = 30
    data_nascimento = "01/01/1993"
    children = 2
    days_employed = 365
    dob_years = 30
    education = "Graduate"
    education_id = 1
    family_status = "Married"
    family_status_id = 1
    gender = "M"
    income_type = "Employed"
    debt = 1000
    total_income = 5000
    purpose = "Home loan"

    # Adiciona o cliente à base de dados
    DataBase.data_base_add_client(nome, idade, data_nascimento, children, days_employed, dob_years, education, education_id,
                                  family_status, family_status_id, gender, income_type, debt, total_income, purpose)

    # Obtém todos os clientes da base de dados
    clientes = DataBase.data_base_get_client()

    # Verifica se o cliente foi adicionado corretamente
    assert len(clientes) == 1
    assert clientes[0].nome == nome
    assert clientes[0].idade == idade

def test_data_base_get_contas_by_id():
    DataBase.data_base_init()  # Inicializa a base de dados
    # Adiciona um cliente
    DataBase.data_base_add_client("Jane Doe", 25, "01/01/1998", 0, 200, 25, "Graduate", 1, "Single", 1, "F", "Employed", 500, 3000, "Car loan")
    
    # Obtém todas as contas do cliente por id
    contas = DataBase.data_base_get_contas_by_id(1)

    # Verifica se a conta foi adicionada corretamente
    assert len(contas) == 1
    assert contas[0].saldo == 500
    assert contas[0].limite_saques == 3

def test_data_base_realizar_transacao():
    DataBase.data_base_init()  # Inicializa a base de dados
    # Adiciona um cliente
    DataBase.data_base_add_client("Jane Doe", 25, "01/01/1998", 0, 200, 25, "Graduate", 1, "Single", 1, "F", "Employed", 500, 3000, "Car loan")
    # Obtém todas as contas do cliente por id
    contas = DataBase.data_base_get_contas_by_id(1)
    
    # Realiza uma transação (depósito)
    DataBase.data_base_realizar_transacao("Jane Doe", contas[0].id, 100)
    # Obtém novamente as contas do cliente
    contas = DataBase.data_base_get_contas_by_id(1)

    # Verifica se o depósito foi realizado corretamente
    assert contas[0].saldo == 600

    # Realiza uma transação (saque)
    DataBase.data_base_realizar_transacao("Jane Doe", contas[0].id, -200)
    # Obtém novamente as contas do cliente
    contas = DataBase.data_base_get_contas_by_id(1)

    # Verifica se o saque foi realizado corretamente
    assert contas[0].saldo == 400
    assert contas[0].limite_saques == 2

def test_data_base_deletar_cliente():
    DataBase.data_base_init()  # Inicializa a base de dados
    # Adiciona um cliente
    DataBase.data_base_add_client("John Doe", 30, "01/01/1993", 2, 365, 30, "Graduate", 1, "Married", 1, "M", "Employed", 1000, 5000, "Home loan")
    # Obtém todos os clientes da base de dados
    clientes = DataBase.data_base_get_client()

    # Deleta o cliente
    DataBase.data_base_deletar_cliente(clientes[0])

    # Obtém novamente todos os clientes
    clientes = DataBase.data_base_get_client()

    # Verifica se o cliente foi deletado corretamente
    assert len(clientes) == 0


