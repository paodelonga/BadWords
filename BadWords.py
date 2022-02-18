import io, sys
import tkinter as tk

from colorama import Back
from colorama import Fore
from colorama import Style
from colorama import init
from os import remove
from os import rename
from os import system as send
from os.path import isfile
from platform import system
from tempfile import gettempdir
from time import sleep
from tkinter import filedialog
from wget import download as down



class App():
	global file, Dict, Letters

	try:
		def clear():
			if 'windows' in system().lower():
				send('cls')
			elif 'linux' in system().lower():
				send('clear')
			else:
				send('clear')

		Letters = {
			'Lower':{'A':{'a','á','à','â','ã'},'E':{'e','é','è','ê'},'I':{'i','í','ì','î'},'O':{'o','ó','ò','ô','õ'}},
			'Upper':{'A':{'A','Á','À','Â','Ã'},'E':{'E','É','È','Ê'},'I':{'I','Í','Ì','Î'},'O':{'O','Ó','Ò','Ô','Õ'}}}
		clear()

		MSG = (
			f"{Fore.GREEN}[PT]{Fore.RESET} Deseja usar sua propria lista com as palavras?\n"
			f"{Fore.GREEN}[PT]{Fore.RESET} Caso não queira, será usada uma lista padrão.\n\n"
			f"{Fore.BLUE}[EN]{Fore.RESET} Want to use your own list of words?\n"
			f"{Fore.BLUE}[EN]{Fore.RESET} If not, a default base list will be used.\n\n")
		print(MSG, Fore.RED)

		ask = input('cmd > ').lower()
		print(Fore.RESET)

		if 'y' in ask.lower() or 's' in ask.lower():
			file = tk.filedialog.askopenfilename(title='Abra o arquivo .txt com os palavrões.')
			if file.endswith('.txt'):
				file = io.open(file, 'r', encoding='UTF-8').read().split()
			elif not file.endswith('.txt'):
				print('\n{0}Invalid file!\nOpen a ".txt" file{1}'.format(Fore.RED, Fore.RESET))
				sys.exit()

		elif 'n' in ask.lower():
			down('https://raw.githubusercontent.com/paodelonga/BadWords/main/database/words.txt', f"{gettempdir()}/words.txt")
			file = io.open(f"{gettempdir()}/words.txt",'r',encoding='UTF-8').read()
			file = file.split()



		else:
			App()

		def VerticalFile():
			Bwords = []
			Bwords.clear()

			# Open new file to write new BadWords
			c = io.open('./converted_vertical.txt','w')

			# Direct write to a file
			c.write('# New BadWords\n') # Write Header
			for w in file:
				Bwords.append(w) # Append ao BadWords to Badwords list
				# Lower Badwords
				for ch in Letters['Lower']['A']:
					if ch in w:
						c.write(w.replace(ch,'4'))
						c.write('\n')
						c.write(w.replace(ch, '@'))
						c.write('\n')
						# print(w.replace(ch,'4'))
						# print(w.replace(ch, '@'))

				for ch in Letters['Lower']['E']:
					if ch in w:
						c.write(w.replace(ch,'3'))
						c.write('\n')
						# print(w.replace(ch,'3'))

				for ch in Letters['Lower']['I']:
					if ch in w:
						c.write(w.replace(ch,'!'))
						c.write('\n')
						c.write(w.replace(ch, '1'))
						c.write('\n')
						# print(w.replace(ch,'!'))
						# print(w.replace(ch,'1'))

				for ch in Letters['Lower']['O']:
					if ch in w:
						c.write(w.replace(ch,'0'))
						c.write('\n')
						# print(w.replace(ch,'0'))


				# Upper Badwords
				for ch in Letters['Upper']['A']:
					if ch in w:
						c.write(w.upper().replace(ch,'4'))
						c.write('\n')
						c.write(w.upper().replace(ch, '@'))
						c.write('\n')
						# print(w.upper().replace(ch,'4'))
						# print(w.upper().replace(ch, '@'))

				for ch in Letters['Upper']['E']:
					if ch in w:
						c.write(w.upper().replace(ch,'3'))
						c.write('\n')
						# print(w.upper().replace(ch,'3'))

				for ch in Letters['Upper']['I']:
					if ch in w:
						c.write(w.upper().replace(ch,'!'))
						c.write('\n')
						c.write(w.upper().replace(ch,'1'))
						c.write('\n')
						# print(w.upper().replace(ch,'!'))
						# print(w.upper().replace(ch,'1'))

				for ch in Letters['Upper']['O']:
					if ch in w:
						c.write(w.upper().replace(ch,'0'))
						c.write('\n')
						# print(w.upper().replace(ch,'0'))

			count = len(Bwords) -1
			print(count) # print count
			sleep(3)
			for bword in Bwords:
				count = count -1

				# Lower BadWords
				for ch in Letters['Lower']['A']:
					Bwords[count] = Bwords[count].replace(ch,'4').replace(ch,'@')
					# print(Bwords[count])
				for ch in Letters['Lower']['E']:
					Bwords[count] = Bwords[count].replace(ch,'3')
					# print(Bwords[count])
				for ch in Letters['Lower']['I']:
					Bwords[count] = Bwords[count].replace(ch,'1').replace(ch,'i')
					# print(Bwords[count])
				for ch in Letters['Lower']['O']:
					Bwords[count] = Bwords[count].replace(ch,'0')
					# print(Bwords[count])

				# Upper BadWords
				for ch in Letters['Upper']['A']:
					Bwords[count] = Bwords[count].replace(ch,'4').replace(ch,'@')
					# print(Bwords[count])
				for ch in Letters['Upper']['E']:
					Bwords[count] = Bwords[count].replace(ch,'3')
					# print(Bwords[count])
				for ch in Letters['Upper']['I']:
					Bwords[count] = Bwords[count].replace(ch,'1').replace(ch,'i')
					# print(Bwords[count])
				for ch in Letters['Upper']['O']:
					Bwords[count] = Bwords[count].replace(ch,'0')
					# print(Bwords[count])
			for b in Bwords:
				c.write(b)
				c.write('\n')
			for b in Bwords:
				c.write(b.upper())
				c.write('\n')
			c.close()
			if isfile('converted_vertical.txt'):
				data = str(io.open('converted_vertical.txt', 'r').read()).rstrip()
				io.open('converted_vertical.txt', 'w').write(data)
				try:
					rename('converted_vertical.txt', f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
				except FileExistsError:
					remove(f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
					rename('converted_vertical.txt', f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
		
		def HorizontalFile():
			Bwords = []
			Bwords.clear()
			chacount = 1

			# Open new file to write new BadWords
			c = io.open('./converted_horizontal.txt','w')

			# Direct write to a file
			for w in file:
				chacount = chacount + 1
				Bwords.append(w) # Append ao BadWords to Badwords list
				# Lower Badwords
				for ch in Letters['Lower']['A']:
					if ch in w:
						c.write(w.replace(ch,'4'))
						c.write(' ')
						c.write(w.replace(ch, '@'))
						c.write(' ')
						# print(w.replace(ch,'4'))
						# print(w.replace(ch, '@'))


				for ch in Letters['Lower']['E']:
					if ch in w:
						c.write(w.replace(ch,'3'))
						c.write(' ')
						# print(w.replace(ch,'3'))


				for ch in Letters['Lower']['I']:
					if ch in w:
						c.write(w.replace(ch,'!'))
						c.write(' ')
						c.write(w.replace(ch, '1'))
						c.write(' ')
						# print(w.replace(ch,'!'))
						# print(w.replace(ch,'1'))


				for ch in Letters['Lower']['O']:
					if ch in w:
						c.write(w.replace(ch,'0'))
						c.write(' ')
						# print(w.replace(ch,'0'))


				# Upper Badwords
				for ch in Letters['Upper']['A']:
					if ch in w:
						c.write(w.upper().replace(ch,'4'))
						c.write(' ')
						c.write(w.upper().replace(ch, '@'))
						c.write(' ')
						# print(w.upper().replace(ch,'4'))
						# print(w.upper().replace(ch, '@'))


				for ch in Letters['Upper']['E']:
					if ch in w:
						c.write(w.upper().replace(ch,'3'))
						c.write(' ')
						# print(w.upper().replace(ch,'3'))


				for ch in Letters['Upper']['I']:
					if ch in w:
						c.write(w.upper().replace(ch,'!'))
						c.write(' ')
						c.write(w.upper().replace(ch,'1'))
						c.write(' ')
						# print(w.upper().replace(ch,'!'))
						# print(w.upper().replace(ch,'1'))


				for ch in Letters['Upper']['O']:
					if ch in w:
						c.write(w.upper().replace(ch,'0'))
						c.write(' ')
						# print(w.upper().replace(ch,'0'))


			count = len(Bwords) -1
			sleep(3)
			chacount = 1
			for bword in Bwords:
				chacount = chacount + 1
				count = count -1

				# Lower BadWords
				for ch in Letters['Lower']['A']:
					Bwords[count] = Bwords[count].replace(ch,'4').replace(ch,'@')
					# print(Bwords[count])
				for ch in Letters['Lower']['E']:
					Bwords[count] = Bwords[count].replace(ch,'3')
					# print(Bwords[count])
				for ch in Letters['Lower']['I']:
					Bwords[count] = Bwords[count].replace(ch,'1').replace(ch,'i')
					# print(Bwords[count])
				for ch in Letters['Lower']['O']:
					Bwords[count] = Bwords[count].replace(ch,'0')
					# print(Bwords[count])

				# Upper BadWords
				for ch in Letters['Upper']['A']:
					Bwords[count] = Bwords[count].replace(ch,'4').replace(ch,'@')
					# print(Bwords[count])
				for ch in Letters['Upper']['E']:
					Bwords[count] = Bwords[count].replace(ch,'3')
					# print(Bwords[count])
				for ch in Letters['Upper']['I']:
					Bwords[count] = Bwords[count].replace(ch,'1').replace(ch,'i')
					# print(Bwords[count])
				for ch in Letters['Upper']['O']:
					Bwords[count] = Bwords[count].replace(ch,'0')
					# print(Bwords[count])

			chacount = 1
			for b in Bwords:
				chacount = chacount + 1
				c.write(b)
				c.write(' ')

			chacount = 1
			for b in Bwords:
				chacount = chacount + 1
				c.write(b.upper())
				c.write(' ')
			c.close()
			if isfile('converted_horizontal.txt'):
				data = str(io.open('converted_horizontal.txt', 'r').read()).rstrip()
				io.open('converted_horizontal.txt', 'w').write(data)
				try:
					rename('converted_horizontal.txt', f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")
				except FileExistsError:
					remove(f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")
					rename('converted_horizontal.txt', f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")

		VerticalFile()
		HorizontalFile()
		clear()
		print(
			f"{Fore.GREEN}[PT]{Fore.RESET} Os arquivos foram salvos na pasta de execução do programa :)\n"
			f"{Fore.BLUE}[EN]{Fore.RESET} The files were saved in the program's execution folder :)\n"
			f'https://www.github.com/paodelonga\n')
		sleep(15)
		try:
			remove(f"{gettempdir()}/words.txt")
		except:
			pass
	except KeyboardInterrupt as ex:
		print(Fore.RESET)
	sys.exit()
App()