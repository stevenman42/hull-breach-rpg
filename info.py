# this is the like stuff that goes above the game in nethack; the name, attributes and whatnot

import string

class Info(object):
	def __init__(self, player):
		self.player = player
		self.dialogue = ["", "", "", "", ""]

	def render(self):
		print("HP: " + str(self.player.health) + "   AC: " + str(self.player.armor))

		print("\n")

	def render_dialogue(self, dialogue=""):
		for d in self.dialogue:
			print(d)
			# if dialogue.strip != "":
			# 	self.dialogue.append(dialogue)
			# 	del self.dialogue[0]

	def add_dialogue(self, dialogue):
		if dialogue.strip != "":
			self.dialogue.append(dialogue)
			del self.dialogue[0]


	def tick(self):
		self.render


