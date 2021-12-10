import io
import os
import platform
import sys
from time import sleep
import tkinter as tk
from tempfile import gettempdir
from tkinter import filedialog


class App():
	global file, Dict, Letters
	Dict = {
		"Yes":{"s", "S", "sim", "Sim", "y", "Y", "yes", "Yes", "yep", "Yep"},
		"No":{"n", "N", "não", "Não", "no", "No", "nop", "Nop"}}
	Letters = {
		"Lower":{"A":{"a","á","à","â","ã"},"E":{"e","é","è","ê"},"I":{"i","í","ì","î"},"O":{"o","ó","ò","ô","õ"}},
		"Upper":{"A":{"A","Á","À","Â","Ã"},"E":{"E","É","È","Ê"},"I":{"I","Í","Ì","Î"},"O":{"O","Ó","Ò","Ô","Õ"}}
	}


	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux" or "Mac" in platform.system():
		os.system("clear")

	try:
		ask = input(
			"Caso não sua lista sera usada uma lista com ~230 palavras.\n"
			"Deseja usar sua lista de palavras? S/N")
	except KeyboardInterrupt as ex:
		App()

	if ask in Dict["Yes"]:
		file = io.open(tk.filedialog.askopenfilename(title="Abra o arquivo .txt com os palavrões."), "r", encoding="UTF-8").read()
		file = file.split()

	elif ask in Dict["No"]:
		os.system(f"curl https://transfer.sh/nyXCju/palavr%C3%B5es.txt --output {gettempdir()}/badword.txt")
		file = io.open(f"{gettempdir()}/badword.txt","r",encoding="UTF-8").read()
		file = file.split()
	else:
		App()

	def VerticalFile():
		Bwords = []
		Bwords.clear()

		# Open new file to write new BadWords
		c = io.open("./converted_vertical.txt","w")

		# Write old BadWords to a new file
		c.write("#============== Old BadWords ==============\n") # Write Header
		for w in file:
			c.write(w)
			c.write("\n")
		c.write("\n\n") # Write a with two lines


		# Direct write to a file
		c.write("#============== New BadWords ==============\n") # Write Header
		for w in file:
			Bwords.append(w) # Append ao BadWords to Badwords list
			# Lower Badwords
			for ch in Letters["Lower"]["A"]:
				if ch in w:
					c.write(w.replace(ch,"4"))
					c.write("\n")
					c.write(w.replace(ch, "@"))
					c.write("\n")
					print(w.replace(ch,"4"))
					print(w.replace(ch, "@"))

			for ch in Letters["Lower"]["E"]:
				if ch in w:
					c.write(w.replace(ch,"3"))
					c.write("\n")
					print(w.replace(ch,"3"))

			for ch in Letters["Lower"]["I"]:
				if ch in w:
					c.write(w.replace(ch,"!"))
					c.write("\n")
					c.write(w.replace(ch, "1"))
					c.write("\n")
					print(w.replace(ch,"!"))
					print(w.replace(ch,"1"))

			for ch in Letters["Lower"]["O"]:
				if ch in w:
					c.write(w.replace(ch,"0"))
					c.write("\n")
					print(w.replace(ch,"0"))


			# Upper Badwords
			for ch in Letters["Upper"]["A"]:
				if ch in w:
					c.write(w.upper().replace(ch,"4"))
					c.write("\n")
					c.write(w.upper().replace(ch, "@"))
					c.write("\n")
					print(w.upper().replace(ch,"4"))
					print(w.upper().replace(ch, "@"))

			for ch in Letters["Upper"]["E"]:
				if ch in w:
					c.write(w.upper().replace(ch,"3"))
					c.write("\n")
					print(w.upper().replace(ch,"3"))

			for ch in Letters["Upper"]["I"]:
				if ch in w:
					c.write(w.upper().replace(ch,"!"))
					c.write("\n")
					c.write(w.upper().replace(ch,"1"))
					c.write("\n")
					print(w.upper().replace(ch,"!"))
					print(w.upper().replace(ch,"1"))

			for ch in Letters["Upper"]["O"]:
				if ch in w:
					c.write(w.upper().replace(ch,"0"))
					c.write("\n")
					print(w.upper().replace(ch,"0"))

		count = len(Bwords) -1
		print(count) # print count
		sleep(3)
		for bword in Bwords:
			count = count -1

			# Lower BadWords
			for ch in Letters["Lower"]["A"]:
				Bwords[count] = Bwords[count].replace(ch,"4").replace(ch,"@")
				print(Bwords[count])
			for ch in Letters["Lower"]["E"]:
				Bwords[count] = Bwords[count].replace(ch,"3")
				print(Bwords[count])
			for ch in Letters["Lower"]["I"]:
				Bwords[count] = Bwords[count].replace(ch,"1").replace(ch,"i")
				print(Bwords[count])
			for ch in Letters["Lower"]["O"]:
				Bwords[count] = Bwords[count].replace(ch,"0")
				print(Bwords[count])

			# Upper BadWords
			for ch in Letters["Upper"]["A"]:
				Bwords[count] = Bwords[count].replace(ch,"4").replace(ch,"@")
				print(Bwords[count])
			for ch in Letters["Upper"]["E"]:
				Bwords[count] = Bwords[count].replace(ch,"3")
				print(Bwords[count])
			for ch in Letters["Upper"]["I"]:
				Bwords[count] = Bwords[count].replace(ch,"1").replace(ch,"i")
				print(Bwords[count])
			for ch in Letters["Upper"]["O"]:
				Bwords[count] = Bwords[count].replace(ch,"0")
				print(Bwords[count])
		for b in Bwords:
			c.write(b)
			c.write("\n")
		for b in Bwords:
			c.write(b.upper())
			c.write("\n")
		c.close()
		if os.path.isfile("converted_vertical.txt"):
			try:
				os.rename("converted_vertical.txt", f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
			except FileExistsError:
				os.remove(f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
				os.rename("converted_vertical.txt", f"converted_vertical_{len((io.open('converted_vertical.txt', 'r').read()).split())}_words.txt")
	
	def HorizontalFile():
		Bwords = []
		Bwords.clear()
		chacount = 1

		# Open new file to write new BadWords
		c = io.open("./converted_horizontal.txt","w")

		# Write old BadWords to a new file
		for w in file:
			c.write(w)
			c.write(" ")

		# Direct write to a file
		for w in file:
			chacount = chacount + 1
			Bwords.append(w) # Append ao BadWords to Badwords list
			# Lower Badwords
			for ch in Letters["Lower"]["A"]:
				if ch in w:
					c.write(w.replace(ch,"4"))
					c.write(" ")
					c.write(w.replace(ch, "@"))
					c.write(" ")
					print(w.replace(ch,"4"))
					print(w.replace(ch, "@"))


			for ch in Letters["Lower"]["E"]:
				if ch in w:
					c.write(w.replace(ch,"3"))
					c.write(" ")
					print(w.replace(ch,"3"))


			for ch in Letters["Lower"]["I"]:
				if ch in w:
					c.write(w.replace(ch,"!"))
					c.write(" ")
					c.write(w.replace(ch, "1"))
					c.write(" ")
					print(w.replace(ch,"!"))
					print(w.replace(ch,"1"))


			for ch in Letters["Lower"]["O"]:
				if ch in w:
					c.write(w.replace(ch,"0"))
					c.write(" ")
					print(w.replace(ch,"0"))


			# Upper Badwords
			for ch in Letters["Upper"]["A"]:
				if ch in w:
					c.write(w.upper().replace(ch,"4"))
					c.write(" ")
					c.write(w.upper().replace(ch, "@"))
					c.write(" ")
					print(w.upper().replace(ch,"4"))
					print(w.upper().replace(ch, "@"))


			for ch in Letters["Upper"]["E"]:
				if ch in w:
					c.write(w.upper().replace(ch,"3"))
					c.write(" ")
					print(w.upper().replace(ch,"3"))


			for ch in Letters["Upper"]["I"]:
				if ch in w:
					c.write(w.upper().replace(ch,"!"))
					c.write(" ")
					c.write(w.upper().replace(ch,"1"))
					c.write(" ")
					print(w.upper().replace(ch,"!"))
					print(w.upper().replace(ch,"1"))


			for ch in Letters["Upper"]["O"]:
				if ch in w:
					c.write(w.upper().replace(ch,"0"))
					c.write(" ")
					print(w.upper().replace(ch,"0"))


		count = len(Bwords) -1
		sleep(3)
		chacount = 1
		for bword in Bwords:
			chacount = chacount + 1
			count = count -1

			# Lower BadWords
			for ch in Letters["Lower"]["A"]:
				Bwords[count] = Bwords[count].replace(ch,"4").replace(ch,"@")
				print(Bwords[count])
			for ch in Letters["Lower"]["E"]:
				Bwords[count] = Bwords[count].replace(ch,"3")
				print(Bwords[count])
			for ch in Letters["Lower"]["I"]:
				Bwords[count] = Bwords[count].replace(ch,"1").replace(ch,"i")
				print(Bwords[count])
			for ch in Letters["Lower"]["O"]:
				Bwords[count] = Bwords[count].replace(ch,"0")
				print(Bwords[count])

			# Upper BadWords
			for ch in Letters["Upper"]["A"]:
				Bwords[count] = Bwords[count].replace(ch,"4").replace(ch,"@")
				print(Bwords[count])
			for ch in Letters["Upper"]["E"]:
				Bwords[count] = Bwords[count].replace(ch,"3")
				print(Bwords[count])
			for ch in Letters["Upper"]["I"]:
				Bwords[count] = Bwords[count].replace(ch,"1").replace(ch,"i")
				print(Bwords[count])
			for ch in Letters["Upper"]["O"]:
				Bwords[count] = Bwords[count].replace(ch,"0")
				print(Bwords[count])

		chacount = 1
		for b in Bwords:
			chacount = chacount + 1
			c.write(b)
			c.write(" ")

		chacount = 1
		for b in Bwords:
			chacount = chacount + 1
			c.write(b.upper())
			c.write(" ")

		c.close()
		if os.path.isfile("converted_horizontal.txt"):
			try:
				os.rename("converted_horizontal.txt", f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")
			except FileExistsError:
				os.remove(f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")
				os.rename("converted_horizontal.txt", f"converted_horizontal_{len((io.open('converted_horizontal.txt', 'r').read()).split())}_words.txt")

	VerticalFile()
	HorizontalFile()
	print("Os arquivos foram salvos na pasta de execução do programa :)\n"
		"da uma olhada lá\n\n"
		"Qualquer coisa me contacta:\n"
		"https://github.com/paodelonga")
	sleep(15)
	sys.exit()
if __name__ == '__main__':
	Application = App()
	App()