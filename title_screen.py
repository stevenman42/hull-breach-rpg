import input as key_input
import os
import characters
from colors import *
import sys
import main

getch = key_input._GetchUnix()

class Title(object):
	def __init__(self):
		self.options = {1: "New game", 2: "Settings", 3: "Quit"}

	def render(self):
		os.system("clear")
		print(color.RED + color.BOLD + "_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    _  _ _  _ _    _       ___  ____ ____ ____ ____ _  _")
		print("| | | |___ |    |    |  | |\/| |___     |  |  |    |__| |  | |    |       |__] |__/ |___ |__| |    |__|")
		print("|_|_| |___ |___ |___ |__| |  | |___     |  |__|    |  | |__| |___ |___    |__] |  \ |___ |  | |___ |  |" + color.END)
		print()

		#self.display_options()
		inn = None
		while inn == None:
			self.display_options()
			inn = self.get_input()

		if inn == "Settings":
			print("NO SETTINGS RIGHT NOW")
		elif inn == "New game":
			self.new_game()
		elif inn == "Quit":
			sys.exit()

	def display_options(self):
		for option in self.options.keys():
			print(str(option) + ": " + self.options[option])

	def get_input(self):
		inn = False
		while inn == False:
			inn = getch.__call__()

		try:
			return self.options[int(inn)]
		except KeyError:
			print("NO")
			return None
		except ValueError:
			print("NO")
			return None

	def new_game(self):
		os.system("clear")
		name = input(color.DARKCYAN + "What is your name? " + color.END)
		print(color.DARKCYAN + "Hi " + color.END + name + color.DARKCYAN + "!\n" + color.END)

		print(color.BLUE + "What class are you? " + color.END)
		for i in range(len(characters.charlist)):
			print(color.BLUE + str(i + 1) + ": " + characters.charlist[i] + color.END)


		inn = None
		while inn == None:
			inn = getch.__call__()

		print()
		
		print(color.BLUE + "You are a " + characters.charlist[int(inn) - 1] + "! Doot doot" + color.END) 

		a = input()

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