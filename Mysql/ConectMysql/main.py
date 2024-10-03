"""
    Libs e a instalação
        mysql-connector-python: pip install mysql-connector-python
        python-dotenv: pip install python-dotenv

    Banco:
        loja
    
    Tabelas:
        cadastroproduto
        cadastrouser
"""

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from tkinter import messagebox
import os
from time import sleep

load_dotenv()

RED   = '\033[31m'
GREEN = '\033[32m'
BLUE  = '\033[34m'
RESET = '\033[0;0m'

def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

LimparTerminal()

def ExecutarConsutas(connection):
    try:
        Tipo = input(f'{BLUE}Tipo: {RESET}')
        QualTabela = input(f'{BLUE}Qual tabela: {RESET}')

        LimparTerminal()
        
        cursor = connection.cursor()
        cursor.execute("SELECT {} FROM {}".format(Tipo, QualTabela))

        # Usa fetchall() para obter todos os resultados
        resultados = cursor.fetchall() 

        for InfoBanco in resultados:
            print(InfoBanco)

    except Error as e:
        print(f"\n{RED}Erro ao executar a consulta: {e} {RESET}")
        messagebox.showerror("ERROR", "ERROR AO EXECUTAR A CONSULTA")

    finally:
        if connection.is_connected():
            cursor.close()
            print(F"\n{GREEN}Cursor fechado!{RESET}")

def ConexaoMysql():
    connection = None
    
    host = os.getenv('MYSQL_HOST')
    database = os.getenv('MYSQL_DATABASE')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')

    try:
        connection = mysql.connector.connect(
            host=host,         # ou o endereço do seu servidor
            database=database, # nome do seu banco de dados
            user=user,         # seu usuário (SE O USER TIVE ROOT PODE COLOCAR ROOT)
            password=password  # sua senha (SE NÃO COLOCOU UMA SENHA, NÃO PRECISA PREENCHE ESSA STRING)
        )

        # Se a conexão for estabelecida
        if connection.is_connected():
            print(f"{GREEN}Conexão bem-sucedida!{RESET}")
            messagebox.showinfo("SUCESSO", "CONEXÃO BEM SUCEDIDA!")
            ExecutarConsutas(connection)

    except Error as e:
        print(f"{RED}Erro ao conectar ao MySQL: {e}{RESET}")
        messagebox.showerror("ERROR", "ERROR AO CONECTAR AO MYSQL")

    finally:
        if connection and connection.is_connected():  # Verifica se a conexão foi inicializada
            connection.close() # Fechar a conexão com o banco
            print(f"\n{GREEN}Conexão fechada!{RESET}")
            
def Main():
    while True:
        Admin = input('Admin: ')
        Pass = input('Pass: ')
        
        if Admin != os.getenv('USER_SYSTEM'):
            print(f'\n{RED}USUARIO INVALIDO!{RESET}')
            sleep(2)
            LimparTerminal()
            
        elif Pass != os.getenv('PASS_SYSTEM'):
            print(f'\n{RED}PASS INVALIDO!{RESET}')
            sleep(2)
            LimparTerminal()
        
        if Admin != os.getenv('USER_SYSTEM') and Pass != os.getenv('PASS_SYSTEM'):
            print(f'\n{RED}USUARIO E PASS INVALIDO!{RESET}')
            sleep(2)
            LimparTerminal()
            
        elif Admin == os.getenv('USER_SYSTEM') and Pass == os.getenv('PASS_SYSTEM'):
            LimparTerminal()
            ConexaoMysql()
            break
Main()