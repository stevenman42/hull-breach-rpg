# this is the like stuff that goes above the game in nethack; the name, attributes and whatnot

import string

class Info(object):
	def __init__(self, player):
		self.player = player
		self.dialogue = ["", "", "", "", "", ""]

	def render(self):
		self.msg = "|  HP: " + str(self.player.health) + "   AC: " + str(self.player.armor) + "   LVL: " + str(self.player.level) + "  |"
		
		print("-" * (len(self.msg)))

		print(self.msg)

		print("-" * (len(self.msg)))

	def render_dialogue(self, dialogue=""):
		for d in self.dialogue:
			print("|  " + d)

		print()


	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.dialogue.append(dialogue)
			del self.dialogue[0]


	def tick(self):
		self.render


