import pyautogui # pip install PyAutoGUI
from time import sleep
from tkinter import messagebox

def LoadArquivo(ARQUIVO):
	try:
		arquivo = open(ARQUIVO, encoding='utf8')

		for fraseAquivo in arquivo:
			pyautogui.typewrite(fraseAquivo)
			pyautogui.press('enter')
	
	except ValueError as err:
		messagebox.showerror("Error: ".format(err), "Não foi possivel carregar o arquivo!: {}".format(ARQUIVO))

def LoadTexto(REPETICAO):
	try:
		texto = input('Seu texto: ')
		LoopMarcado = REPETICAO

		print('\n5 segundos pra iniciar\n')
		sleep(5)

		while True:
			pyautogui.typewrite(texto)
			pyautogui.press('enter')
			LoopMarcado -= 1

			if LoopMarcado == 0:
				break
	
	except ValueError as err:
		messagebox.showerror("Error: ".format(err), "Não foi possivel carregar o seu texto!: {}".format(texto)) 
