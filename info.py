# this is the like stuff that goes above the game in nethack; the name, attributes and whatnot


class Info(object):
	def __init__(self, player):
		self.player = player

	def render(self):
		print("HP: " + str(self.player.health) + "   AC: " + str(self.player.armor))

		print("\n\n\n")

	def tick(self):
		self.render