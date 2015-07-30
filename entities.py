class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	def __init__(self):
		pass

	def move(self, game, deltaX, deltaY):
		print("movin'")

		try:
			game.entities[self.yPos][self.xPos].remove(self)
			game.entity_icons[self.yPos][self.xPos].remove(self.icon)
			self.xPos += deltaX
			self.yPos += deltaY
			game.entities[self.yPos][self.xPos].append(self)
			game.entity_icons[self.yPos][self.xPos].append(self.icon)
		except IndexError:
			self.xPos -= deltaX
			self.yPos -= deltaY
			game.entities[self.yPos][self.xPos] = game.player
			game.entity_icons[self.yPos][self.xPos] = game.player.icon


class Book(Entity):

	def __init__(self, description):
		self.description = description
		self.icon = "B"

