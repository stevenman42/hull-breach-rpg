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
		self.screenwidth = 0


	def render(self):
		(self.screenwidth, height) = console.getTerminalSize()
		self.msg = self.player.name + " the " + self.player.title + " |  Strength: " + str(self.player.health) + "   Defense: " + str(self.player.armor) + "   Level: " + str(self.player.level) + "  |"
		self.width = len(self.msg)
		horiz_buffer = " " * ((self.screenwidth - self.width) / 2)
		
		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

		print(horiz_buffer + self.msg)

		print(horiz_buffer + (" " * len(self.player.name + " the  " + self.player.title)) + "-" * (len(self.msg) - len(self.player.name + " the  " + self.player.title)))

		health_percent = self.player.health*1.0 / self.player.maxhealth
		print(health_percent)
		if health_percent*100 >= 75:
			print(horiz_buffer + "Health: " + color.GREEN + "=" * int(((self.width) - 8) * health_percent) + color.END)
		elif health_percent*100 < 75 and health_percent*100 >= 25:
			print(horiz_buffer + "Health: " + color.YELLOW + "=" * int(((self.width) - 8) * health_percent) + color.END)
		elif health_percent*100 < 25:
			print(horiz_buffer + "Health: " + color.RED + "=" * int(((self.width) - 8) * health_percent) + color.END)

		hunger_percent = self.player.hunger*1.0 / self.player.maxhunger
		# print(horiz_buffer + "  Food: " + "=" * int(((width/2) + 2) * hunger_percent))

		if hunger_percent*100 >= 75:
			print(horiz_buffer + "  Food: " + color.GREEN + "=" * int(((self.width) - 8) * hunger_percent) + color.END)
		elif hunger_percent*100 < 75 and hunger_percent*100 >= 25:
			print(horiz_buffer + "  Food: " + color.YELLOW + "=" * int(((self.width) - 8) * hunger_percent) + color.END)
		elif hunger_percent*100 < 25:
			print(horiz_buffer + "  Food: " + color.RED + "=" * int(((self.width) - 8) * hunger_percent) + color.END)

	def render_dialogue(self, dialogue=""):
		print(color.BLUE + " " + "-"*(self.screenwidth-2) + color.END)
		for d in self.visible_dialogue:
			if len(d) > self.screenwidth:
				for i in range(len(d)):
					if i % (self.screenwidth-8) == 0:
						print(color.BLUE + " |  " + color.END + color.WHITE + d[i:i+self.screenwidth-8] + color.END + " "*(self.screenwidth - len(d[i:i+self.screenwidth-8]) - 7) + color.BLUE + " |" + color.END)
			else:
				print(color.BLUE + " |  " + color.END + color.WHITE + d + color.END + " "*(self.screenwidth - len(d) - 7) + color.BLUE + " |" + color.END)

		print(color.BLUE + " " + "-"*(self.screenwidth-2) + color.END)

		print("\n")

	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.visible_dialogue.append(dialogue)
			self.dialogue.append(dialogue)
			del self.visible_dialogue[0]


	def scroll_back(self):
		# idk why it's 9
		length = len(self.dialogue)
		if length - 2 - (9) - self.scroll >= 0:
			for i in range(len(self.visible_dialogue)):
				self.visible_dialogue[i] = self.dialogue[length - 1 - (9-i) - self.scroll]
			self.scroll += 1
		else:
			return False

	def scroll_forward(self):
		length = len(self.dialogue)
		if length - 2 - self.scroll < length:
			for i in range(len(self.visible_dialogue)):
				try:
					self.visible_dialogue[i] = self.dialogue[length - 1 - (8-i) - self.scroll]
				except IndexError:
					return
			self.scroll -= 1
		else:
			return False

	def tick(self):
		self.render


