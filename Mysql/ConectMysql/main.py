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

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[36m'
RESET = '\033[0;0m'

ListaInfoTable = []

def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ExecutarConsutas(connection):
    try:
        LimparTerminal()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cadastrouser")

        # Usa fetchall() para obter todos os resultados
        resultados = cursor.fetchall()
        
        if not resultados:
            print(f"{RED}\nNenhum resultado encontrado!\n{RESET}")
            
        else:
            for linhaMySql in resultados:
                ListaInfoTable.append(linhaMySql)

            print('\nResultados da consulta\n')
            for ListaPythonMySql in ListaInfoTable:
                print(ListaPythonMySql)

        input(f"\n{BLUE}Pressione Enter para sair...{RESET}")

    except Error as e:
        print(f"\n{RED}Erro ao executar a consulta: {e} {RESET}")
        messagebox.showerror("ERROR", "ERRO AO EXECUTAR A CONSULTA")

    finally:
        if connection.is_connected():
            cursor.close()
            print(f"\n{GREEN}Cursor fechado!{RESET}")

def MostrarTables(connection):
    LimparTerminal()

    try:
        cursorTabelasExistentes = connection.cursor()
        cursorTabelasExistentes.execute("SHOW TABLES")
        
        # Limpa a lista antes de adicionar novos resultados
        ListaInfoTable.clear()
        
        # Usa fetchall() para obter todos os resultados
        resultadosTabelasExistentes = cursorTabelasExistentes.fetchall()

        if not resultadosTabelasExistentes:
            print(f"{RED}\nNenhuma tabela encontrada!{RESET}")
            
        else:
            print("\nTabelas existentes no banco de dados\n")
            for linhaMySql in resultadosTabelasExistentes:
                print(linhaMySql[0])

    except Error as e:
        print(f"{RED}Erro ao mostrar tabelas: {e}{RESET}")
        messagebox.showerror("ERROR", "ERRO AO MOSTRAR TABELAS")

    finally:
        if connection.is_connected():
            cursorTabelasExistentes.close()
            print(f"\n{GREEN}Cursor de tabelas fechado!{RESET}")

    
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
            messagebox.showinfo("SUCESSO", "CONEXÃO BEM SUCEDIDA!")

            while True:
                print('\n1° Mostrar tabelas')
                print('2° Consultar')
                print('3° Sair')

                try:
                    CodigoNav = int(input('\nNav: '))
                except ValueError:
                    print(f"{RED}Por favor, insira um número válido.{RESET}")
                    continue

                match CodigoNav:
                    case 1:
                        MostrarTables(connection)
                    case 2:
                        ExecutarConsutas(connection)
                    case 3:
                        print(f"{GREEN}Saindo...{RESET}")
                        break
                    case _:
                        print(f"{RED}Opção inválida!{RESET}")

    except Error as e:
        print(f"{RED}Erro ao conectar ao MySQL: {e}{RESET}")
        messagebox.showerror("ERROR", "ERROR AO CONECTAR AO MYSQL")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print(f"\n{GREEN}Conexão fechada!{RESET}")

def Main():
    while True:
        Admin = input('Admin: ')
        Pass = input('Pass: ')
        
        if Admin != os.getenv('USER_SYSTEM') or Pass != os.getenv('PASS_SYSTEM'):
            print(f'\n{RED}USUARIO OU PASS INVALIDO!{RESET}')
            sleep(2)
            LimparTerminal()
        else:
            LimparTerminal()
            ConexaoMysql()
            break
Main()
