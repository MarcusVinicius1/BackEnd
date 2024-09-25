from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Crie a janela principal do aplicativo
app = tk.Tk()
app.configure(background="#333", padx=10, pady=10)
app.title("Calculator")
app.minsize(480, 400)
app.maxsize(480, 400)
FontSize = 50

DiasSemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# Colocar a janela no centro da tela
def CenterWindow(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    win.geometry(f'{width}x{height}+{x}+{y}')

# Formatando o número com duas casas decimais
def FormatTime(valor):
    return f'{valor:02}'

# Definir e atualiza a hora e data
def UpdateTime():
    try:
        # Obter a hora atual
        NewDate = datetime.now()
        
        # Formatar a hora e a data
        Hora = FormatTime(NewDate.hour)
        Minuto = FormatTime(NewDate.minute)
        Segundo = FormatTime(NewDate.second)
        Dia = FormatTime(NewDate.day)
        Mes = FormatTime(NewDate.month)
        Ano = NewDate.year
        Semana = NewDate.weekday()

        HoraFormat = f'{Hora}:{Minuto}:{Segundo}'
        DataFormat = f'{Dia}/{Mes}/{Ano}'
        SemanaFormat = DiasSemana[Semana + 1]

        # Atualize o rótulo com o novo horário
        LabelTime.config(text=HoraFormat)
        LabelDate.config(text=DataFormat)
        LabelSemana.config(text=SemanaFormat)

        # Chame esta função novamente após 1000 ms (1 segundo)
        app.after(1000, UpdateTime)
    
    except ValueError:
        messagebox.showerror("ERROR", "ERROR AO MOSTRAR A HORA E A DATA!")

# Canpo pra inserir o hora e data
LabelTime = tk.Label(app, text="", font=("sans-serif", FontSize, "bold"), fg="white", bg="#333")
LabelTime.pack(pady=10)

LabelDate = tk.Label(app, text="", font=("sans-serif", FontSize, "bold"), fg="white", bg="#333")
LabelDate.pack(pady=10)

LabelSemana = tk.Label(app, text="", font=("sans-serif", FontSize, "bold"), fg="white", bg="#333")
LabelSemana.pack(pady=10)

CenterWindow(app)
UpdateTime()
app.mainloop()
