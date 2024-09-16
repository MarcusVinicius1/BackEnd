"""
Instalar as libs

-- psutil          = pip install psutil
-- python-dotenv   = pip install python-dotenv
"""
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import re
import uuid
import platform
import psutil
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from time import sleep
import logging

# Configuração de logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

os.system('cls' if os.name == 'nt' else 'clear')

class SystemScannerApp:
    Separacao = '------------------'

    def __init__(self, master):
        self.master = master
        self.master.title("Suporte online")
        self.master.configure(background="#222")
        self.master.minsize(width=700, height=470)
        self.master.maxsize(width=700, height=470)
        self.master.iconbitmap('SuporteOnline.ico')

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED, background="black", fg="white")

        scan_button = tk.Button(master, text="Escanear Sistema", bg="#333", border=False, fg="white", font=("sans-serif", "13", "bold"), command=self.scan_system)
        scan_button.pack(side=tk.LEFT, padx=10, pady=10)

        send_button = tk.Button(master, text="Enviar Informações", bg="#333", border=False, fg="white", font=("sans-serif", "13", "bold"), command=self.send_info)
        send_button.pack(side=tk.LEFT, padx=10, pady=10)

        ajuda_button = tk.Button(master, text="Ajuda", bg="#333", border=False, fg="white", font=("sans-serif", "13", "bold"), command=self.ask_for_help)
        ajuda_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.center_window()

    def center_window(self):
        """
        Função para centralizar as janelas
        """

        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    def get_info_system(self):
        """
        Função para coletar informações do sistema

        Tipos de informações que serão coletados

        -- MAC
        -- IP
        -- Host
        -- Sistema
        -- Processador
        -- Release
        -- Versão
        -- Arquitetura

        -- Total RAM
        -- RAM disponível
        -- Uso da RAM

        -- Partições
        """

        try:
            Mac = ':'.join(re.findall('..', '%012x' % uuid.getnode())) 

            ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip.connect(("8.8.8.8", 80))
            ip_address = ip.getsockname()[0]
            ip.close()

            host = platform.node()
            system = platform.system()
            processor = platform.processor()
            release = platform.release()
            version = platform.version()
            architecture = platform.machine()

            ram = psutil.virtual_memory()
            total_ram = ram.total / (1024 ** 3)
            available_ram = ram.available / (1024 ** 3)
            used_ram = ram.used / (1024 ** 3)

            partitions_info = ""
            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    total_storage = usage.total / (1024 ** 3)
                    used_storage = usage.used / (1024 ** 3)
                    free_storage = usage.free / (1024 ** 3)

                    partitions_info += f"\t-- Device: {partition.device}, Mountpoint: {partition.mountpoint}, File system: {partition.fstype}\n\n\tTotal armazenamento: {total_storage:.2f} GB\n\n\tArmazenamento usado: {used_storage:.2f} GB\n\n\tArmazenamento livre: {free_storage:.2f} GB\n\t{self.Separacao}\n\n"
                except Exception as e:
                    logging.error(f"Erro ao obter informações da partição {partition.device}", exc_info=True)
                    partitions_info += f"\t-- Device: {partition.device}, Mountpoint: {partition.mountpoint}, File system: {partition.fstype}\n\n\tErro ao obter informações\n\t{self.Separacao}\n\n"
                    messagebox.showerror("Erro", f"Erro ao obter informações da partição {partition.device}.\nEssa partição não vai está a lista, pode enviar mesmo assim!")

            info = f"""
            MAC: {Mac}
            IP Address: {ip_address}
            Host: {host}
            Sistema: {system}
            Processador: {processor}
            Release: {release}
            Versão: {version}
            Arquitetura: {architecture}

            Total RAM: {total_ram:.2f} GB
            RAM disponível: {available_ram:.2f} GB
            Uso da RAM: {used_ram:.2f} GB

            {self.Separacao}

            Partições:
            {partitions_info}
            """

            return info

        except Exception as e:
            logging.error("Erro ao obter informações do sistema", exc_info=True)
            messagebox.showerror("Erro", "Não foi possível obter as informações do sistema!")

    def send_email(self, info):
        """
        Função para enviar informações pelo email
        """

        sender_email = os.getenv('EMAIL_USER')
        receiver_email = os.getenv('EMAIL_DESTINATARIO')
        password = os.getenv('EMAIL_PASSWORD')

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Informações do Sistema"

        message.attach(MIMEText(info, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()

            messagebox.showinfo("Enviado", f"E-mail enviado para {receiver_email}")

        except Exception as e:
            logging.error("Erro ao enviar o e-mail", exc_info=True)
            messagebox.showerror("Erro", "Não foi possível enviar o e-mail!")

    def scan_system(self):
        info = self.get_info_system()
        self.text_area.config(state=tk.NORMAL, font=("sans-serif", "13", "bold"))
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.INSERT, info)
        self.text_area.config(state=tk.DISABLED)

    def send_info(self):
        """
        Função para enviar informações escaneadas, se o campo de vazio ele não enviar e mostrar uma notificação dizendo que o campo está vazio
        """

        info = self.text_area.get(1.0, tk.END).strip()
        if not info:
            messagebox.showwarning("Alerta", "O campo de informações está vazio. Primeiro, escaneie o sistema antes de enviar!")
        else:
            self.send_email(info)

    def ask_for_help(self):
        print('Pedido de ajuda solicitado. Implementar a funcionalidade aqui.')

def main():
    """
    Função principal e login
    """

    load_dotenv()
    Login = os.getenv('USER')
    Key = os.getenv('KEY')
    Tentativas = 3

    while True:
        Login_Input = input('Login: ').lower()
        Key_Input = input('Key: ').lower()

        if Tentativas <= 0:
            messagebox.showwarning("Alerta", "Houve muitas tentativas de login. Aguarde um pouco para tentar novamente!")
            NovaTentativa = 5

            while NovaTentativa > 0:
                print(f"Você tem {NovaTentativa}s para tentar de novo", end="\r")
                sleep(1)
                NovaTentativa -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            break

        elif Login_Input != Login:
            Tentativas -= 1
            messagebox.showwarning("Alerta", f"SENHA INVÁLIDA! Tentativas restantes: {Tentativas}")
        
        elif Key_Input != Key:
            Tentativas -= 1
            messagebox.showwarning("Alerta", f"CHAVE INVÁLIDA! Tentativas restantes: {Tentativas}")

        else:
            root = tk.Tk()
            app = SystemScannerApp(root)
            root.mainloop()
            break

if __name__ == "__main__":
    main()

