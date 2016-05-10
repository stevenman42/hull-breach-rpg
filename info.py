# this is the like stuff that goes above the game in nethack; the name, attributes and whatnot

import string
from colors import *
import console
import sys

class Info(object):
	def __init__(self, player):
		self.player = player
		self.dialogue = []
		self.visible_dialogue = ["", "", "", "", "", "", "", ""]
		self.scroll = -1
		


	def render(self):
		(width, height) = console.getTerminalSize()
		self.msg = self.player.name + " the " + self.player.title + " |  Strength: " + str(self.player.health) + "   Defense: " + str(self.player.armor) + "   Level: " + str(self.player.level) + "  |"
		self.width = len(self.msg)
		horiz_buffer = " " * ((width - self.width) / 2)
		
		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

		print(horiz_buffer + self.msg)

		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

		health_percent = self.player.health*1.0 / self.player.maxhealth
		print(health_percent)
		if health_percent*100 >= 75:
			print(horiz_buffer + "Health: " + color.GREEN + "=" * int(((width/2) + 2) * health_percent) + color.END)
		elif health_percent*100 < 75 and health_percent*100 >= 25:
			print(horiz_buffer + "Health: " + color.YELLOW + "=" * int(((width/2) + 2) * health_percent) + color.END)
		elif health_percent*100 < 25:
			print(horiz_buffer + "Health: " + color.RED + "=" * int(((width/2) + 2) * health_percent) + color.END)

		hunger_percent = self.player.hunger*1.0 / self.player.maxhunger
		# print(horiz_buffer + "  Food: " + "=" * int(((width/2) + 2) * hunger_percent))

		if hunger_percent*100 >= 75:
			print(horiz_buffer + "  Food: " + color.GREEN + "=" * int(((width/2) + 2) * hunger_percent) + color.END)
		elif hunger_percent*100 < 75 and hunger_percent*100 >= 25:
			print(horiz_buffer + "  Food: " + color.YELLOW + "=" * int(((width/2) + 2) * hunger_percent) + color.END)
		elif hunger_percent*100 < 25:
			print(horiz_buffer + "  Food: " + color.RED + "=" * int(((width/2) + 2) * hunger_percent) + color.END)

	def render_dialogue(self, dialogue=""):
		for d in self.visible_dialogue:
			print(color.WHITE + "|  " + d + color.END)

		print("")


	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.visible_dialogue.append(dialogue)
			self.dialogue.append(dialogue)
			del self.visible_dialogue[0]


	def scroll_back(self):
		# idk why it's 9
		length = len(self.dialogue)
		if length - 1 - (9) - self.scroll >= 0:
			for i in range(len(self.visible_dialogue)):
				self.visible_dialogue[i] = self.dialogue[length - 1 - (9-i) - self.scroll]
			self.scroll += 1
		else:
			return False

	def scroll_forward(self):
		length = len(self.dialogue)
		if length - 2 - self.scroll < length:
			for i in range(len(self.visible_dialogue)):
				self.visible_dialogue[i] = self.dialogue[length - 1 - (8-i) - self.scroll]
			self.scroll -= 1
		else:
			return False

	def tick(self):
		self.render


