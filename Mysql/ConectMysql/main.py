"""
    Libs e a instalação
        mysql-connector-python: pip install mysql-connector-python
        python-dotenv: pip install python-dotenv

    Banco:
        loja
    
    Tabelas:
        cadastroproduto
        cadastrouser
        adminacess
"""
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[36m'
RESET = '\033[0;0m'

ListaInfoTable = []

# Função para limpar o terminal
def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

LimparTerminal()

# Função para validar se a entrada é um número inteiro
def validar_entrada_inteiro(prompt, tipo='int'):
    while True:
        try:
            entrada = input(prompt)
            if tipo == 'int':
                return int(entrada)
            elif tipo == 'float':
                return float(entrada)
        except ValueError:
            print(f"{RED}Entrada inválida. Por favor, insira um número válido.{RESET}")

# Função para realizar operações SQL de forma reutilizável
def executar_query(connection, query, params=None, fetch=False):
    try:
        cursor = connection.cursor()
        cursor.execute(query, params) if params else cursor.execute(query)
        
        if fetch:
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        else:
            connection.commit()
            cursor.close()
    except Error as e:
        print(f"{RED}Erro ao executar a query: {e}{RESET}")

# Função para exibir as tabelas do banco
def MostrarTables(connection):
    LimparTerminal()
    print("\nTabelas existentes no banco de dados:\n")
    tabelas = executar_query(connection, "SHOW TABLES", fetch=True)
    if tabelas:
        for tabela in tabelas:
            print(tabela[0])
    else:
        print(f"{RED}Nenhuma tabela encontrada!{RESET}")
    
    input(f"\n{BLUE}Pressione Enter para retornar...{RESET}")

# Função para exibir os dados da tabela 'cadastrouser'
def VerTabelas(connection):
    LimparTerminal()
    print("\nResultados da consulta:\n")
    dados = executar_query(connection, "SELECT * FROM cadastrouser", fetch=True)
    if dados:
        for linha in dados:
            print(linha)
    else:
        print(f"{RED}Nenhum resultado encontrado!{RESET}")

# Função para inserir um novo produto
def InserirNovoProduto(connection):
    LimparTerminal()
    print("\nInserir novo produto:\n")
    nome = input("Nome: ")
    preco = validar_entrada_inteiro("Preço: ", tipo='float')
    quantidade = validar_entrada_inteiro("Quantidade: ", tipo='int')
    
    executar_query(connection, "INSERT INTO cadastroproduto (Nome, Preco, Qtd) VALUES (%s, %s, %s)", (nome, preco, quantidade))
    print(f"\n{GREEN}Novo produto inserido com sucesso!{RESET}")

# Função para alterar dados do usuário
def AlterarDadosDoUsuario(connection):
    VerTabelas(connection)
    print('\nAlterar dados de usuário:\n')
    CodigoUsuario = validar_entrada_inteiro("Código do usuário: ", tipo='int')
    nomeNovo = input("Novo nome: ")
    novoSobrenome = input("Novo sobrenome: ")

    try:
        executar_query(connection, "UPDATE cadastrouser SET Nome=%s, Sobrenome=%s WHERE id=%s", (nomeNovo, novoSobrenome, CodigoUsuario))
        print(f"\n{GREEN}Dados do usuário alterados com sucesso!{RESET}")
    except Error as e:
        print(f"{RED}Erro ao atualizar os dados: {e}{RESET}")

# Função principal para a interação com o banco de dados
def ExecutarConsultas(connection):
    try:
        AcoesBanco = [
            'Ver tabelas',  # Ok
            'Inserir novo produto',  # Ok
            'Alterar dados de um usuário'
        ]

        print("\nEscolha uma ação:")
        for index, acao in enumerate(AcoesBanco, start=1):
            print(f"{index}° {acao}")

        Codigo = validar_entrada_inteiro("\nNav: ", tipo='int')

        match Codigo:
            case 1:
                VerTabelas(connection)
            case 2:
                InserirNovoProduto(connection)
            case 3:
                AlterarDadosDoUsuario(connection)

        input(f"\n{BLUE}Pressione Enter para sair...{RESET}")

    except Error as e:
        print(f"\n{RED}Erro ao executar a consulta: {e} {RESET}")

# Função para a conexão com o MySQL
def ConexaoMysql():
    connection = None
    host = os.getenv('MYSQL_HOST')
    database = os.getenv('MYSQL_DATABASE')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            print(f"{GREEN}Conexão bem-sucedida!{RESET}")

            while True:
                print('\n1. Mostrar tabelas')
                print('2. Consultar')
                print('3. Sair')

                CodigoNav = validar_entrada_inteiro('\nNav: ', tipo='int')

                match CodigoNav:
                    case 1:
                        MostrarTables(connection)
                    case 2:
                        ExecutarConsultas(connection)
                    case 3:
                        print(f"{GREEN}Saindo...{RESET}")
                        break
                    case _:
                        print(f"{RED}Opção inválida!{RESET}")
                        sleep(1)

    except Error as e:
        print(f"{RED}Erro ao conectar ao MySQL: {e}{RESET}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print(f"\n{GREEN}Conexão fechada!{RESET}")

# Função principal de autenticação
def Main():
    while True:
        Admin = input('Admin: ')
        Pass = input('Pass: ')
        
        if Admin != os.getenv('USER_SYSTEM') or Pass != os.getenv('PASS_SYSTEM'):
            print(f'\n{RED}USUÁRIO OU SENHA INVÁLIDO!{RESET}')
            sleep(2)
            LimparTerminal()
        else:
            LimparTerminal()
            ConexaoMysql()
            break

Main()
