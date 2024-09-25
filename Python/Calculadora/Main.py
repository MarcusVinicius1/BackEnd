import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.configure(background="#333", padx=10, pady=10)
app.title("Calculator")
app.minsize(295, 280)
app.maxsize(295, 280)

expression = ""

def update_expression(value):
    global expression
    
    expression += str(value)
    display.set(expression)

def calculate():
    global expression
    
    try:
        result = str(eval(expression))
        display.set(result)
        expression = result
        
    except Exception:
        messagebox.showerror('Error', "Expressão invalida!")
        expression = ""

def clear():
    global expression
    
    expression = ""
    display.set("")

def backspace():
    global expression
    
    expression = expression[:-1]
    display.set(expression)
    
def pocentagem():
    global expression
    
    try:
        if expression:
            result = str(eval(expression)) + "%"
            display.set(result)
            expression = ""
            
        else:
            messagebox.showerror('Error', "Error ao calcular!")
            
    except Exception:
        messagebox.showerror('Error', "Expressão invalida!")
        expression = ""

def toggle_sign():
    global expression
    
    if expression:
        try:
            last_number = str(eval(expression))
            if last_number:
                last_number = -float(last_number)
                expression = str(last_number)
                display.set(expression)
                
        except Exception:
            messagebox.showerror('Error', "Expressão invalida!")
            expression = ""

# Display
display = tk.StringVar()
visor = tk.Label(app, textvariable=display, background="white", padx=10, pady=10, width=23, font=("bold", 15))
visor.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('%', 1, 0), ('C', 1, 1), ('/', 1, 2), ('back', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=calculate)
    elif text == 'C':
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=clear)
    elif text == 'back':
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=backspace)
    elif text == '%':
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=pocentagem)
    elif text == '+/-':
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=toggle_sign)
    else:
        btn = tk.Button(app, text=text, border=False, bg="black", fg="white", width=5, height=1, font=("bold", 15),
                        command=lambda value=text: update_expression(value))
    btn.grid(row=row + 100, column=col)

app.mainloop()
