# Projeto Banco com Python

Movido pelos estudos sobre a linguagem Python do curso "Formação Python" da DIO, decidi tentar criar um software de um banco capaz de criar usuários, criar contas para os usuários, permitir a realização de transações e calcular o risco de crédito dos usuários.

## Descrição
O projeto consiste em um sistema gráfico para criação e exclusão de clientes e contas de um banco. As contas podem ser submetidas às ações "sacar" e "depositar". Etapas executadas e futuras:
1. Transformação das classes "Cliente" e "Conta" em módulos a serem utilizadoss
2. Implementar banco de dados SQL usando SQLAIchemy
3. Implementar uma versão com banco de dados MongoDB Atlas
4. Será utilizada inteligencia artificial e machine learning para calcular o risco de crédito dosclientes com base na referência "https://github.com/ThiagoFQ/Python/blob/main/credit-scoring-bank.ipynb".

## Etapas que esse projeto passou
Ao longo dos estudos do curso "Formação Python" da DIO, passamos por diversos passos de conhecimento e estudo. Esse projeto, portanto, veio passando por mudanças em sua estrutura e a linha do tempo vem apresentada abaixo:

| Linha do tempo | Eventos  |
|----------------|----------|
| 02/07/2023     | Transformou-se as classes "Cliente" e "Conta" em dois módulos usando os conceitos aprendidos no curso "Formação Python". Pode ser que seja nescessário efetuar "pip install Cliente" e "pip install Conta"   |
| 03/07/2023     | Transformou-se as classes "Cliente" e "Conta" em duas classses do SQLAIchemy de forma tal que as contas são associadas aos Clientes no modelo um (Cliente) para vários (Contas)   |
| 04/07/2023     | Excluiu-se a interface gráfica para dar acesso a api Flask para integrações em ambientes online   |

        
## Bibliotecas e Frameworks utilizados
-PyQT5:

    pip install pyqt5

-Flask:

    pip install Flask

-SQLAIchemy:

    pip install SQLAlchemy

-PyTest:

    pip install pytest

-datetime: Integrado ao Python
-sys: Integrado ao python 
setuptools:

    pip install setuptools

## Entidades do projeto
- Conta: Classe que representa uma conta bancária, com os métodos: imprimir_saldo, imprimir_historico, sacar, depositar
- Cliente: Classe que representa um cliente do banco, com os métodos: adicionar_conta, listar_contas, remover_conta
- RpositorioClientes: Classe que representa um repositóirio de vários clientes do banco, com os métodos: adicionar_cliente, listar_clientes, excluir_cliente, listar_contas_cliente, criar_conta, transacionar_conta, apagar_conta, buscar_cliente_id, buscar_conta_cliente.

## Como executar esse código:
1. Instalação das bibliotecas nescessárias:
    a. Flask [Microframework para otimizar a api]: 

            pip install Flask

    b. SQLAIchemy [Framework para otimizar o acesso ao banco de dados relacional]: 

            pip install SQLAlchemy

    c. pytest [Testes unitários e automatizados]: 
                
                pip install pytest

    d. pyqt5 [Usado para elaboração das interfaces gráficas]: 

            pip install pyqt5

2. Execução do software:

        python SWBanco.py

3. Login e senha de acesso ao sistema de interfaces gráficas: "Admin"
