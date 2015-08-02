# this is the like stuff that goes above the game in nethack; the name, attributes and whatnot

import string
from colors import *
import console

class Info(object):
	def __init__(self, player):
		self.player = player
		self.dialogue = ["", "", "", "", "", ""]


	def render(self):
		(width, height) = console.getTerminalSize()
		self.msg = self.player.name + " the " + self.player.title + " |  Hit Points: " + str(self.player.health) + "   Defense: " + str(self.player.armor) + "   Level: " + str(self.player.level) + "  |"
		self.width = len(self.msg)
		horiz_buffer = " " * ((width - self.width) / 2)
		
		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

		print(horiz_buffer + self.msg)

		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

	def render_dialogue(self, dialogue=""):
		for d in self.dialogue:
			print(color.WHITE + "|  " + d + color.END)

		print("")


	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.dialogue.append(dialogue)
			del self.dialogue[0]


	def tick(self):
		self.render


