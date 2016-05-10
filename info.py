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
		for d in self.dialogue:
			print(color.WHITE + "|  " + d + color.END)

		print("")


	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.dialogue.append(dialogue)
			del self.dialogue[0]


	def tick(self):
		self.render


