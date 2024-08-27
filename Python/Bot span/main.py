from time import sleep
import os
from funcoes import LoadArquivo
from funcoes import LoadTexto

RED = '\033[31m'
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

def LimparTerminal():
	os.system('nt' if os.name == 'clear' else 'cls')

while True:
	LimparTerminal()

	ListaHistoria = [
		'1° Texto',
		'2° Historia / Filme',
		'3° Sair do programa'
	]

	HistoriasFilmes = [
		'1° Shrek (Filme)','2° Pinoquio (Historia)'
	]

	for historiasList in ListaHistoria:
		print(historiasList)

	TipoSpan = int(input('\nQue tipo de span: '))

	texto = ''
	if TipoSpan == 3:
		break

	loop = int(input('\nReptição: '))
	loopMarcado = loop

	if loopMarcado > 0:
		while loop > 0:
			if loopMarcado == 0:
				loopMarcado = 0
				break
			
			else:
				if TipoSpan == 1:
					LoadTexto(loopMarcado)

				elif TipoSpan == 2:
					LimparTerminal()
					print('\n-- Seleção de texto --\n')
					for histfilm in HistoriasFilmes:
						print(histfilm)

					EscolhaTexto = int(input('\nQual texto deseja enviar?: '))
					
					print('\n5 segundos pra iniciar\n')
					for Index in range(1, 6):
						print(Index)
						sleep(1)

					if EscolhaTexto == 1:
						LoadArquivo('HistFilm/shrek.txt')
					
					if EscolhaTexto == 2:
						LoadArquivo('HistFilm/pinoquio.txt')
					
					break

			print(loopMarcado)
			loopMarcado -= 1
			sleep(1)

			if loopMarcado == 0:
				print(f"\n{GREEN}Texto enviado!{RESET}\n")
			
			break
	else:
		print(f'\n{RED}Canpo vazio, insira pelo menos 1 de valor de repetição{RESET}\n')