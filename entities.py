class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	def __init__(self):
		pass

	def move(self, game, deltaX, deltaY):
		print("movin'")

		try:
			game.map[self.yPos][self.xPos] = "."
			self.xPos += deltaX
			self.yPos += deltaY
			game.map[self.yPos][self.xPos] = "0"
		except IndexError:
			self.xPos -= deltaX
			self.yPos -= deltaY
			game.map[self.yPos][self.xPos] = "0"