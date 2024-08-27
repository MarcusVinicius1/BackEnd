import pyautogui # pip install PyAutoGUI
from time import sleep

def LoadArquivo(ARQUIVO):
	arquivo = open(ARQUIVO, encoding='utf8')

	for fraseAquivo in arquivo:
		pyautogui.typewrite(fraseAquivo)
		pyautogui.press('enter')

def LoadTexto(REPETICAO):
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