import input as key_input
import os
import characters
from colors import *
import sys
import main
import console

getch = key_input._GetchUnix()

class Title(object):
	def __init__(self):
		self.options = ["New game", "Load game", "Settings", "Quit"]
		self.option = 0
		self.selected_option = self.options[self.option]

	def render(self):

		os.system("clear")

		
		inn = None
		while inn != " ":
			
			self.display_title()
			self.display_options()
			inn = getch.__call__()
			if inn == "down":
				os.system("clear")
				if (self.option < len(self.options)):
					self.option += 1
					try:
						self.selected_option = self.options[self.option]
					except IndexError:
						self.option -= 1
			elif inn == "up":
				os.system("clear")
				if (self.option > 0):
					self.option -= 1
					try:
						self.selected_option = self.options[self.option]
					except IndexError:
						self.option += 1


		if self.selected_option == "Settings":
			print("NO SETTINGS RIGHT NOW")
		elif self.selected_option == "New game":
			self.new_game()
		elif self.selected_option == "Load game":
			print("CAN'T LOAD GAMES RIGHT NOW")
		elif self.selected_option == "Quit":
			sys.exit()

	def display_title(self):
		(width, height) = console.getTerminalSize()
		vert_buffer = "\n" * int((height)/2 - 8)
		print(vert_buffer)
		buffer = " " * int((width - len("_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    _  _ _  _ _    _       ___  ____ ____ ____ ____ _  _")) / 2)


		print(color.RED + color.BOLD + buffer + "_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    _  _ _  _ _    _       ___  ____ ____ ____ ____ _  _")
		print(buffer + "| | | |___ |    |    |  | |\/| |___     |  |  |    |__| |  | |    |       |__] |__/ |___ |__| |    |__|")
		print(buffer + "|_|_| |___ |___ |___ |__| |  | |___     |  |__|    |  | |__| |___ |___    |__] |  \ |___ |  | |___ |  |" + color.END)
		print("\n")

	def display_options(self):
		for option in self.options:
			(width, height) = console.getTerminalSize()

			buffer = " " * int((width - len(option)) / 2)
			if option == self.selected_option:
				print(color.BLUE + color.BOLD + buffer + option + color.END)
			else:
				print(color.YELLOW + buffer + option + color.END)

			print("")

	def get_input(self):
		inn = False
		while inn == False:
			inn = getch.__call__()
			print(inn)
			if inn == " ":
				print("tru")


	def new_game(self):
		os.system("clear")
		name = raw_input(color.DARKCYAN + "What is your name? " + color.END)
		print(color.DARKCYAN + "Hi " + color.END + name + color.DARKCYAN + "!\n" + color.END)

		print(color.BLUE + "What class are you? " + color.END)
		for i in range(len(characters.charlist)):
			print(color.BLUE + str(i + 1) + ": " + characters.charlist[i] + color.END)


		inn = None
		while inn == None:
			inn = getch.__call__()
			print(inn)

		print("")
		
		print(color.BLUE + "You are a " + characters.charlist[int(inn) - 1] + "! Doot doot" + color.END) 

		a = raw_input()

		if inn == "1":
			main.run(characters.Knight(None, 1, 1))
		elif inn == "2":
			main.run(characters.Wizard(None, 1, 1))
		elif inn == "3":
			main.run(characters.Gunner(None, 1, 1))
		elif inn == "4":
			main.run(characters.Rogue(None, 1, 1))

title = Title()
title.render()