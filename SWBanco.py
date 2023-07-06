
from flask import Flask, jsonify, request
from DataBase import DataBase

app = Flask(__name__)

# Inicializa a base de dados
DataBase.data_base_init()

# Teste:
# Adiciona um novo cliente chamado João
DataBase.data_base_add_client(nome="João", idade=30, data_nascimento="15/05/1992", children=2, days_employed=2000, dob_years=30,
                    education="Superior", education_id=1, family_status="Casado", family_status_id=1,
                    gender="M", income_type="Assalariado", debt=0, total_income=5000, purpose="Compra de imóvel")

# Adiciona uma nova conta para o cliente João
DataBase.data_base_add_conta(client_id=1, saldo=1000, limite_saques=5)

@app.route('/clientes', methods=['GET'])
def api_get_clientes():
    try:
        """Rota para obter todos os clientes

        Returns:
            JSON: JSON com todos os clientes
        """
        clientes = DataBase.data_base_get_client()
        clientes_json = {
            "clientes": [
                {
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "idade": cliente.idade
                }
                for cliente in clientes
            ]
        }
        return jsonify(clientes_json), 200  # 200 OK
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

@app.route('/clientes/add', methods=['POST'])
def api_add_clientes():
    try:
        """Rota para adicionar um novo cliente

        Returns:
            str: Retorna apenas 'Sucesso ao add cliente' caso tenha conseguido adicionar o dado ao banco de dados
        """

        # Extrair os dados do cliente do corpo da requisição
        data = request.get_json()

        # Adicionar o novo cliente ao banco de dados
        nome = data.get('nome')
        idade = data.get('idade')
        data_nascimento = data.get('data_nascimento')
        children = data.get('children')
        days_employed = data.get('days_employed')
        dob_years = data.get('dob_years')
        education = data.get('education')
        education_id = data.get('education_id')
        family_status = data.get('family_status')
        family_status_id = data.get('family_status_id')
        gender = data.get('gender')
        income_type = data.get('income_type')
        debt = data.get('debt')
        total_income = data.get('total_income')
        purpose = data.get('purpose')

        DataBase.data_base_add_client(nome=nome, idade=idade, data_nascimento=data_nascimento,
                                    children=children, days_employed=days_employed, dob_years=dob_years,
                                    education=education, education_id=education_id, family_status=family_status,
                                    family_status_id=family_status_id, gender=gender, income_type=income_type,
                                    debt=debt, total_income=total_income, purpose=purpose)

        return 'Sucesso ao add cliente', 201  # 201 Created
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

@app.route('/contas/add', methods=['POST'])
def api_add_conta():

    try:
        # Extrair os dados da conta do corpo da requisição
        data = request.get_json()
        id = data.get('id')
        saldo = data.get('saldo')
        limite_saques = data.get('limite_saques')

        DataBase.data_base_add_conta(client_id=id, saldo=saldo, limite_saques=limite_saques)

        return 'Sucesso ao add conta!', 201  # 201 Created
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

@app.route('/clientes/<int:cliente_id>/contas', methods=['GET'])
def api_get_contas_cliente(cliente_id):
    try:
        # Obter as contas do cliente com base no ID
        contas = DataBase.data_base_get_contas_by_id(cliente_id)

        # Criar a estrutura JSON com as informações das contas
        contas_json = {
            "cliente_id": cliente_id,
            "contas": [
                {
                    "id": conta.id,
                    "saldo": conta.saldo,
                    "limite_saques": conta.limite_saques
                }
                for conta in contas
            ]
        }

        return jsonify(contas_json), 200  # 200 OK
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error
>>>>>>> v003

@app.route('/clientes/<int:cliente_id>/contas/transaction', methods=['PUT'])
def api_update_conta_cliente(cliente_id):
    try:
        # Obter as contas do cliente com base no ID
        contas = DataBase.data_base_get_contas_by_id(cliente_id)

        # Extrair os dados da transação do corpo da requisição
        data = request.get_json()
        id = data.get('id')
        valor = data.get('valor')

        for conta in contas:
            if conta.id == id:
                DataBase.data_base_realizar_transacao(conta.id, valor)
                break

        # Obter as contas do cliente com base no ID
        conta = DataBase.data_base_get_conta_by_conta_id(id)
        # Criar a estrutura JSON com as informações da conta
        conta_json = {
            "id": conta.id,
            "saldo": conta.saldo,
            "limite_saques": conta.limite_saques
        }

        return jsonify(conta_json), 200  # 200 OK
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

@app.route('/clientes/excluir', methods=['POST'])
def api_clientes_excluir():
    try:
        # Extrair os dados do cliente do corpo da requisição
        data = request.get_json()
        id = data.get('id')
        cliente = DataBase.data_base_get_client_by_id(id)
        DataBase.data_base_deletar_cliente(cliente)

        return 'Cliente excluído com sucesso!', 200  # 200 OK
>>>>>>> v003
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

@app.route('/contas/excluir', methods=['POST'])
def api_contas_excluir():
    try:
        # Extrair os dados da conta do corpo da requisição
        data = request.get_json()
        id_conta = data.get('id_conta')
        conta = DataBase.data_base_get_conta_by_conta_id(id_conta)
        DataBase.data_base_deletar_conta(conta)
        # Criar a estrutura JSON com as informações da conta
        conta_json = {
            "id": conta.id,
            "saldo": conta.saldo,
            "limite_saques": conta.limite_saques,
            "status": "deletada"
        }

        return jsonify(conta_json), 200  # 200 OK
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error

if __name__ == '__main__':
    app.run()
