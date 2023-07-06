from datetime import datetime as dt
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import json

# Cria uma conexão com o banco de dados SQLite em memória
engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    data_nascimento = Column(Date)
    children = Column(Integer)
    days_employed = Column(Integer)
    dob_years = Column(Integer)
    education = Column(String)
    education_id = Column(Integer)
    family_status = Column(String)
    family_status_id = Column(Integer)
    gender = Column(String)
    income_type = Column(String)
    debt = Column(Integer)
    total_income = Column(Integer)
    purpose = Column(String)

    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    saldo = Column(Integer)
    limite_saques = Column(Integer)
    historico = Column(String)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship('Cliente', back_populates='contas')

    def __init__(self, saldo=0, limite_saques=3):
        self.saldo = saldo
        self.limite_saques = limite_saques
        self.historico = json.dumps([])  # Histórico padrão é uma lista vazia convertida para JSON

    def sacar(self, valor):
        if self.saldo >= valor and self.limite_saques > 0:
            self.saldo -= valor
            self.limite_saques -= 1
            historico = json.loads(self.historico)
            historico.append(f"Saque: - R$ {valor:.2f}")
            self.historico = json.dumps(historico)
        else:
            print("Saldo insuficiente ou limite de saques atingido.")

    def depositar(self, valor):
        self.saldo += valor
        historico = json.loads(self.historico)
        historico.append(f"Depósito: + R$ {valor:.2f}")
        self.historico = json.dumps(historico)

    def get_historico(self):
        return self.historico

class DataBase():

    def data_base_init():
        """data_base_init

        Description: Inicializa a base de dados
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        """

        # Cria as tabelas no banco de dados
        Base.metadata.create_all(engine)


    def data_base_add_client(nome, idade, data_nascimento, children, days_employed, dob_years, education, education_id,
                            family_status, family_status_id, gender, income_type, debt, total_income, purpose):
        """data_base_add_client

        Description: Adiciona um novo cliente a base de dados
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        Args:
            nome (int): Nome do cliente
            idade (int): idade do cliente
            data_nascimento (string): Data de nascimento do cliente
            children (int): Quantidade de filhos do cliente
            days_employed (int): Tempo de trabalho do cliente em dias
            dob_years (int): idade do cliente
            education (string): Nível de escolaridade do cliente
            education_id (int): Identificador único do nível de escolaridade do cliente
            family_status (string): Status civil do cliente
            family_status_id (int): Identificador único do nível de escolaridade do cliente
            gender (string): Gênero (M, F, XMA)
            income_type (string): Tipo de renda do cliente
            debt (int): Débito
            total_income (int): Renda mensal do cliente
            purpose (string): Propósito que o cliente pode vir a desejar pegar uma linha de crédito
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Converte a string de data em um objeto de data Python
        data_nascimento = dt.strptime(data_nascimento, "%d/%m/%Y").date()
        cliente = Cliente(nome=nome, idade = idade, data_nascimento = data_nascimento, children = children, days_employed = days_employed,
                        dob_years = dob_years, education = education, education_id = education_id, family_status = family_status, 
                        family_status_id = family_status_id, gender = gender, income_type = income_type, debt = debt, 
                        total_income = total_income, purpose = purpose)
        
        session.add(cliente)
        session.commit()

        # Fecha a sessão
        session.close()
    
    def data_base_add_conta(client_id, saldo, limite_saques):
        """Função para add uma nova conta a base de dados

        Args:
            client_id (int): id do cliente no banco
            saldo (float): saldo da conta
            limite_saques (int): limite de saques da conta
        """
        Session = sessionmaker(bind=engine)
        session = Session()   
        # Retorna todas as contas de um cliente específico
        cliente = session.query(Cliente).filter_by(id=client_id).first()
        print("Nome do cliente: ", cliente.nome)
        conta = Conta(saldo ,limite_saques)
        
        # Adicione a conta ao cliente
        cliente.contas.append(conta)

        # Cria uma sessão para interagir com o banco de dados
        session.add(conta)
        session.commit()

        # Fecha a sessão
        session.close()     

    def data_base_get_client():
        """data_base_get_client

        Description: Retorna todos os clientes da base de dados
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retorna todos os clientes
        clientes = session.query(Cliente).all()
        for cliente in clientes:
            print(f'Cliente: {cliente.nome}')

        # Fecha a sessão
        session.close()

        return clientes
    
    def data_base_get_client_by_id(client_id):

        """Função para retornar um cliente específico do banco de dados

        Returns:
            Cliente: Cliente cujo id é especificado como parâmetro
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retorna todas as contas de um cliente específico
        cliente = session.query(Cliente).filter_by(id=client_id).first()

        # Fecha a sessão
        session.close()
        
        return cliente        

    def data_base_get_contas_by_id(client_id):
        """data_base_get_contas_by_id

        Description: Retorna todas as contas de um cliente específico com base no id do cliente
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        Args:
            client_id (int): identificador único do cliente no banco de dados
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retorna todas as contas de um cliente específico
        cliente = session.query(Cliente).filter_by(id=client_id).first()
        contas = cliente.contas
        for conta in contas:
            print(f'Conta do cliente {cliente.nome}: {conta.saldo}')

        # Fecha a sessão
        session.close()
        
        return contas

    def data_base_get_contas_by_name(client_name):
        """data_base_get_contas_by_name

        Description: Retorna todas as contas de um cliente específico com base no nome do cliente
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        Args:
            client_name (String): Nome do cliente
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retorna todas as contas de um cliente específico
        cliente = session.query(Cliente).filter_by(name=client_name).first()
        contas = cliente.contas
        for conta in contas:
            print(f'Conta do cliente {cliente.nome}: {conta.numero}')

        # Fecha a sessão
        session.close()
        
        return contas

    def data_base_get_conta_by_conta_id(conta_id):

        """Função para retornar a conta buscando pelo id

        Returns:
            Conta: conta pesquisada pelo id
        """
 
        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retorna a conta
        conta = session.query(Conta).filter_by(id=conta_id).first()     

        # Commits não precisam ser feitos quando consultas são realizadas
        # session.commit()

        # Fecha a sessão
        session.close()

        return conta  

    def data_base_realizar_transacao(conta_id, valor):
        """data_base_realizar_transacao

        Description: Realiza uma transação em uma conta específica do cliente especificado como parâmetro da função
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        Args:
            client_name (string): Nome do cliente
            conta_id (int): identificador único da conta no banco de dados
            valor (int): valor para sacar/ depositar
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Valor dentro da function: ", valor)

        # Retorna a conta
        conta = session.query(Conta).filter_by(id=conta_id).first()

        if valor >= 0:
            conta.depositar(valor)
        else:
            valor = valor*(-1)
            conta.sacar(valor)

        session.commit()

        # Fecha a sessão
        session.close()

    def data_base_deletar_conta(conta):
        """data_base_deletar_conta

        Description: Deleta uma conta específica da base de dados
        Author: Filipe Mesel Lobo Costa Cardoso
        Date: 03/07/2023

        Args:
            conta (Conta): Conta a ser apagada
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Remove uma conta
        session.delete(conta)
        session.commit()

    def data_base_deletar_cliente(cliente):
        """data_base_deletar_cliente

        Args:
            cliente (Cliente): Cliente a ser excluido da base de dados
        """

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        session = Session()

        # Remove um cliente
        session.delete(cliente)
        session.commit()

        # Fecha a sessão
        session.close()