import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QSpinBox, QComboBox, QPushButton, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QComboBox, QApplication, QListWidget, QListWidgetItem, QHBoxLayout
from datetime import datetime as dt
from Conta.Conta import Conta
from Cliente.Cliente import Cliente
from Repositorio_de_Clientes import RepositorioClientes

repositorio = RepositorioClientes()

class RealizarTranzactionWindow(QWidget):
    def __init__(self, client_id, conta_id, repositorio):
        super().__init__()
        self.setWindowTitle("Clients List Window")
        self.client_id = client_id
        self.conta_id = conta_id
        self.repositorio = repositorio
        
        # Widgets
        self.label_valor = QLabel("Valor:")

        self.input_valor = QSpinBox()
        self.input_valor.setMinimum(0)
        self.input_valor.setMaximum(999999)
        self.input_valor.setSingleStep(1)

        self.button_conta_sacar = QPushButton("Sacar!!!")

        self.button_conta_depositar = QPushButton("Depositar!!!")

        self.button_voltar = QPushButton("Voltar")

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.label_valor, 0, 0)
        layout.addWidget(self.input_valor, 0, 1)

        layout.addWidget(self.button_conta_sacar, 1, 0, 1, 1)  # Ajuste das células ocupadas pelo botão Sacar
        layout.addWidget(self.button_conta_depositar, 1, 1, 1, 1)  # Ajuste das células ocupadas pelo botão Depositar

        layout.addWidget(self.button_voltar, 2, 0, 1, 2)  # Ajuste das células ocupadas pelo botão Voltar

        self.setLayout(layout)

        # Signals
        self.button_conta_sacar.clicked.connect(self.function_conta_sacar)
        self.button_conta_depositar.clicked.connect(self.function_conta_depositar)
        self.button_voltar.clicked.connect(self.function_conta_votlar)

    def function_conta_sacar(self):
        print("Sacar!!")
        self.repositorio.transacionar_conta(self.client_id, self.conta_id, (-1*self.input_valor.value()))
        contas = self.repositorio.listar_contas_cliente(self.client_id)
        for conta in contas:
            print(conta.saldo)
            print("---------------------------")

    def function_conta_depositar(self):
        print("Depositar!!")
        self.repositorio.transacionar_conta(self.client_id, self.conta_id, self.input_valor.value())
        contas = self.repositorio.listar_contas_cliente(self.client_id)
        for conta in contas:
            print(conta.saldo)
            print("---------------------------")
    
    def function_conta_votlar(self):
        print("Voltar")
        self.main_window = ListContasWindow(self.client_id, self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()





class ListContasWindow(QWidget):
    def __init__(self, client_id, repositorio):
        super().__init__()
        self.setWindowTitle("Clients List Window")
        self.client_id = client_id
        self.repositorio = repositorio
        cliente = self.repositorio.buscar_cliente_id(self.client_id)

        # Widget para exibir a lista de clientes
        self.list_widget = QListWidget()

        # Botão "Voltar"
        self.button_voltar = QPushButton("Voltar")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Lista de Contas do cliente"))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.button_voltar)
        self.setLayout(layout)
        
        # Preencher a lista de contas ao abrir a janela
        self.preencher_lista_contas()

        # Conectar o botão "Voltar" à função de voltar
        self.button_voltar.clicked.connect(self.voltar)

    def preencher_lista_contas(self):
        self.list_widget.clear()
        contas = self.repositorio.listar_contas_cliente(self.client_id)
        for conta in contas:
            item = QListWidgetItem()

            # Criar um widget para o item da lista
            item_widget = QWidget()

            # Layout do widget do item
            item_layout = QVBoxLayout(item_widget)

            # Rótulo com o id do conta
            label_id = QLabel(str(conta.id))
            item_layout.addWidget(label_id)

            # Rótulo com o saldo do conta
            label_saldo = QLabel(str(conta.saldo))
            item_layout.addWidget(label_saldo)

            # Rótulo com o limite_saques do conta
            label_limite_saques = QLabel(str(conta.limite_saques))
            item_layout.addWidget(label_limite_saques)

            # Layout horizontal para os botões
            button_layout = QHBoxLayout()

            # Botão "Excluir conta"
            button_excluir = QPushButton("Excluir Conta")
            button_excluir.clicked.connect(lambda _, conta=conta: self.excluir_conta(conta))
            button_layout.addWidget(button_excluir)

            # Botão "Listar Contas"
            button_realizar_transacao = QPushButton("Realizar transação bancária")
            button_realizar_transacao.clicked.connect(lambda _, conta=conta: self.realizar_transacao(conta))
            button_layout.addWidget(button_realizar_transacao)

            # Adicionar o layout de botões ao layout do item
            item_layout.addLayout(button_layout)

            # Adicionar o widget ao item da lista
            item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)
        
        

    def excluir_conta(self, conta):
        # Implemente a função de Criar conta aqui
        print("Excluir a conta")
        self.repositorio.apagar_conta(self.client_id, conta.id)
        self.main_window = ListContasWindow(self.client_id, self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

    def realizar_transacao(self, conta):
        # Implemente a função de Criar conta aqui
        print("Realizar transação bancária")
        self.main_window = RealizarTranzactionWindow(self.client_id, conta.id, self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

    def voltar(self):
        # Implementar a lógica de voltar para a tela anterior
        print("Voltar")
        self.main_window = ListClientsWindow(self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

class CreateContaWindow(QWidget):
    def __init__(self, client_id, repositorio):
        super().__init__()
        self.setWindowTitle("Clients List Window")
        self.client_id = client_id
        self.repositorio = repositorio
        
        # Widgets
        self.label_saldo = QLabel("Saldo:")
        self.label_limite_saques = QLabel("Limite de saques:")

        self.input_saldo = QSpinBox()
        self.input_saldo.setMinimum(-999999)
        self.input_saldo.setMaximum(999999)
        self.input_saldo.setSingleStep(1)

        self.input_limite_saques = QSpinBox()
        self.input_limite_saques.setMinimum(0)
        self.input_limite_saques.setMaximum(62)
        self.input_limite_saques.setSingleStep(1)

        self.button_add_new_conta = QPushButton("Cadastrar conta ao cliente")

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.label_saldo, 0, 0)
        layout.addWidget(self.input_saldo, 0, 1)

        layout.addWidget(self.label_limite_saques, 1, 0)
        layout.addWidget(self.input_limite_saques, 1, 1)

        layout.addWidget(self.button_add_new_conta, 2, 0, 1, 2)

        self.setLayout(layout)

        # Signals
        self.button_add_new_conta.clicked.connect(self.function_add_new_conta)

    def function_add_new_conta(self):
        print("client_id: ", self.client_id)
        self.repositorio.criar_conta(self.client_id, 
                                     self.input_saldo.value(), 
                                     self.input_limite_saques.value())
        print("Conta criada com sucesso!")
        contas = self.repositorio.listar_contas_cliente(self.client_id)
        for conta in contas:
            print(conta.id)
            print(conta.saldo)
            print(conta.limite_saques)
        
        # Implementar a lógica de voltar para a tela anterior
        print("Voltar")
        self.main_window = ListClientsWindow(self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

class ListClientsWindow(QWidget):
    def __init__(self, repo_clientes):
        super().__init__()
        self.setWindowTitle("Clients List Window")
        self.repositorio = repositorio

        ##Teste
        cliente = Cliente("João", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                        "Assalariado", False, 5000, "Comprar uma casa")
        cliente2 = Cliente("Bruno", 30, "01/01/1990", 2, 1000, 30, "Ensino Médio", 1, "Casado", 1, "Masculino",
                        "Assalariado", False, 5000, "Comprar uma casa")
        self.repositorio.adicionar_cliente(cliente)
        self.repositorio.adicionar_cliente(cliente2)
        
        # Widget para exibir a lista de clientes
        self.list_widget = QListWidget()

        # Botão "Voltar"
        self.button_voltar = QPushButton("Voltar")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Lista de Clientes"))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.button_voltar)
        self.setLayout(layout)
        
        # Preencher a lista de clientes ao abrir a janela
        self.preencher_lista_clientes()

        # Conectar o botão "Voltar" à função de voltar
        self.button_voltar.clicked.connect(self.voltar)

    def preencher_lista_clientes(self):
        self.list_widget.clear()
        clientes = self.repositorio.listar_clientes()
        for cliente in clientes:
            item = QListWidgetItem()

            # Criar um widget para o item da lista
            item_widget = QWidget()

            # Layout do widget do item
            item_layout = QVBoxLayout(item_widget)

            # Rótulo com o nome do cliente
            label_nome = QLabel(cliente.nome)
            item_layout.addWidget(label_nome)

            # Layout horizontal para os botões
            button_layout = QHBoxLayout()

            # Botão "Excluir Cliente"
            button_excluir = QPushButton("Excluir Cliente")
            button_excluir.clicked.connect(lambda _, cliente=cliente: self.excluir_cliente(cliente))
            button_layout.addWidget(button_excluir)

            # Botão "Listar Contas"
            button_listar_contas = QPushButton("Listar Contas")
            button_listar_contas.clicked.connect(lambda _, cliente=cliente: self.listar_contas(cliente))
            button_layout.addWidget(button_listar_contas)

            # Botão "Criar Contas"
            button_criar_conta = QPushButton("Criar nova Conta")
            button_criar_conta.clicked.connect(lambda _, cliente=cliente: self.criar_conta(cliente))
            button_layout.addWidget(button_criar_conta)

            # Botão "Calcular risco de crédito"
            button_calcular_risco_credito = QPushButton("Calcualr Risco de Crédito")
            button_calcular_risco_credito.clicked.connect(lambda _, cliente=cliente: self.calcular_risco_credito(cliente))
            button_layout.addWidget(button_calcular_risco_credito)

            # Adicionar o layout de botões ao layout do item
            item_layout.addLayout(button_layout)

            # Adicionar o widget ao item da lista
            item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)



    def excluir_cliente(self, cliente):
        self.repositorio.excluir_cliente(cliente.id)
        self.preencher_lista_clientes()

    def calcular_risco_credito(self, cliente):
        # Implemente a função de Criar conta aqui
        print("Criar o cálculo do risco de crédito")

    def criar_conta(self, cliente):
        # Implemente a função de Criar conta aqui
        print("Criar as conta do cliente")
        cliente_id = cliente.id
        self.main_window = CreateContaWindow(cliente_id, self.repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

    def listar_contas(self, cliente):
        # Implemente a função de listar contas aqui
        print("Listar as contas do cliente")
        contas = self.repositorio.listar_contas_cliente(cliente.id)
        if len(contas) != 0:
            for conta in contas:
                print(conta.saldo)
            self.main_window = ListContasWindow(cliente.id, self.repositorio)
            self.main_window.setGeometry(100, 100, 600, 400)
            self.main_window.show()
            self.close()
        else:
            print("Cliente novo")
        pass

    def voltar(self):
        # Implementar a lógica de voltar para a tela anterior
        print("Voltar")
        self.main_window = MainWindow()
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()



class AddClientWindow(QWidget):
    def __init__(self, repositorio):
        super().__init__()
        self.setWindowTitle("Add new Client Window")
        self.repositorio = repositorio
        
        # Widgets
        self.label_name = QLabel("Nome:")
        self.label_data_nascimento = QLabel("Data de nascimento:")
        self.label_children = QLabel("Número de dependentes (Crianças):")
        self.label_days_employed = QLabel("Número de dias trabalhados:")
        self.label_dob_years = QLabel("Idade:")
        self.label_education = QLabel("Nível de escolaridade:")
        self.label_family_status = QLabel("Status cívil:")
        self.label_gender = QLabel("Gênero:")
        self.label_income_type = QLabel("Status do emprego:")
        self.label_debt = QLabel("Dívida:")
        self.label_total_income = QLabel("Renda mensal:")
        self.label_purpose = QLabel("Propósito:")

        self.input_name = QLineEdit()

        self.input_data_nascimento = QLineEdit()

        self.input_children = QSpinBox()
        self.input_children.setMinimum(0)
        self.input_children.setMaximum(20)
        self.input_children.setSingleStep(1)

        self.input_days_employed = QSpinBox()
        self.input_days_employed.setMinimum(0)
        self.input_days_employed.setMaximum(926185831)
        self.input_days_employed.setSingleStep(1)

        self.input_dob_years = QSpinBox()
        self.input_dob_years.setMinimum(0)
        self.input_dob_years.setMaximum(100)
        self.input_dob_years.setSingleStep(1)

        self.input_education = QComboBox()
        self.input_education.addItem("Bachelor's Degree")
        self.input_education.addItem("secondary education")
        self.input_education.addItem("Some College")
        self.input_education.addItem("Primary Education")
        self.input_education.addItem("Graduate Degree")

        self.input_family_status = QComboBox()
        self.input_family_status.addItem("married")
        self.input_family_status.addItem("civil partnership")
        self.input_family_status.addItem("widow / widower")
        self.input_family_status.addItem("divorced")
        self.input_family_status.addItem("unmarried")

        self.input_gender = QComboBox()
        self.input_gender.addItem("M")
        self.input_gender.addItem("F")
        self.input_gender.addItem("XMA")

        self.input_income_type = QComboBox()
        self.input_income_type.addItem("employee")
        self.input_income_type.addItem("retiree")
        self.input_income_type.addItem("business")
        self.input_income_type.addItem("civil servant")
        self.input_income_type.addItem("unemployed")
        self.input_income_type.addItem("entrepreneur")
        self.input_income_type.addItem("student")
        self.input_income_type.addItem("paternity / maternity leave")

        self.input_debt = QComboBox()
        self.input_debt.addItem("True")
        self.input_debt.addItem("False")

        self.input_total_income = QSpinBox()
        self.input_total_income.setMinimum(-99990999)
        self.input_total_income.setMaximum(926185831)
        self.input_total_income.setSingleStep(1)

        self.input_purpose = QLineEdit()

        self.button_add_new_client = QPushButton("Cadastrar cliente")

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.input_name, 0, 1)

        layout.addWidget(self.label_data_nascimento, 1, 0)
        layout.addWidget(self.input_data_nascimento, 1, 1)

        layout.addWidget(self.label_children, 2, 0)
        layout.addWidget(self.input_children, 2, 1)

        layout.addWidget(self.label_days_employed, 3, 0)
        layout.addWidget(self.input_days_employed, 3, 1)

        layout.addWidget(self.label_dob_years, 4, 0)
        layout.addWidget(self.input_dob_years, 4, 1)

        layout.addWidget(self.label_education, 5, 0)
        layout.addWidget(self.input_education, 5, 1)

        layout.addWidget(self.label_family_status, 6, 0)
        layout.addWidget(self.input_family_status, 6, 1)

        layout.addWidget(self.label_gender, 7, 0)
        layout.addWidget(self.input_gender, 7, 1)

        layout.addWidget(self.label_income_type, 8, 0)
        layout.addWidget(self.input_income_type, 8, 1)

        layout.addWidget(self.label_debt, 9, 0)
        layout.addWidget(self.input_debt, 9, 1)

        layout.addWidget(self.label_total_income, 10, 0)
        layout.addWidget(self.input_total_income, 10, 1)

        layout.addWidget(self.label_purpose, 11, 0)
        layout.addWidget(self.input_purpose, 11, 1)

        layout.addWidget(self.button_add_new_client, 12, 0, 1, 2)

        self.setLayout(layout)

        # Signals
        self.button_add_new_client.clicked.connect(self.function_add_new_client)

    def function_add_new_client(self):
        #valor = self.input_dob_years.value()
        cliente = Cliente(nome=self.input_name.text(), 
                          idade=self.input_dob_years.value(), 
                          data_nascimento=self.input_data_nascimento.text(),
                          children=self.input_children.value(), 
                          days_employed=self.input_days_employed.value(), 
                          dob_years=self.input_dob_years.value(), 
                          education=self.input_education.currentText(), 
                          education_id=self.input_education.currentIndex(), 
                          family_status=self.input_family_status.currentText(), 
                          family_status_id=self.input_family_status.currentIndex(), 
                          gender=self.input_gender.currentText(),
                          income_type=self.input_income_type.currentIndex(),
                          debt=self.input_income_type.currentIndex(), 
                          total_income=self.input_total_income.value(), 
                          purpose=self.input_purpose.text())
        self.repositorio.adicionar_cliente(cliente)
        clientes = self.repositorio.listar_clientes()
        print("Cliente adicionado!")
        for cliente in clientes:
            print(cliente.nome)
        self.main_window = MainWindow()
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        
        # Widgets
        self.label_username = QLabel("Username:")
        self.label_password = QLabel("Password:")
        self.input_username = QLineEdit()
        self.input_password = QLineEdit()
        self.button_login = QPushButton("Login")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
        
        self.setLayout(layout)
        
        # Signals
        self.button_login.clicked.connect(self.login)
    
    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        
        if username == "Admin" and password == "Admin":
            print("Login successful!")
            self.open_main_window()  # Abrir a nova janela
        else:
            print("Invalid username or password!")
            # Adicione aqui a lógica para exibir uma mensagem de erro no aplicativo
    
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        # Widgets
        self.button_list_clients = QPushButton("Listar Cliente")
        self.button_add_client = QPushButton("Adicionar novo cliente")
        self.button_logout = QPushButton("Logout")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button_list_clients)
        layout.addWidget(self.button_add_client)
        layout.addWidget(self.button_logout)
        
        self.setLayout(layout)

        # Signals
        self.button_list_clients.clicked.connect(self.function_list_clients)
        self.button_add_client.clicked.connect(self.function_add_client)
        self.button_logout.clicked.connect(self.function_logout)
    
    def function_list_clients(self):
        print("Listar clientes")
        self.main_window = ListClientsWindow(repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()
    
    def function_add_client(self):
        print("Add clientes")
        self.main_window = AddClientWindow(repositorio)
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()
    
    def function_logout(self):
        print("Logout")
        self.main_window = LoginWindow()
        self.main_window.setGeometry(100, 100, 600, 400)
        self.main_window.show()
        self.close()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec_())
