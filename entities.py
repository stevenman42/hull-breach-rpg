class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	def __init__(self):
		self.walkable = True
		self.whackable = False

	def move(self, game, deltaX, deltaY):

		can_move = True
		can_whack = False

		for i in game.entities[self.yPos + deltaY][self.xPos + deltaX]:
			if i.walkable == False:
				can_move = False
			if i.whackable == True:
				can_move = False
				can_whack = True

		if can_move:

			try:
				game.entities[self.yPos][self.xPos].remove(self)
				game.entity_icons[self.yPos][self.xPos].remove(self.icon)
				self.xPos += deltaX
				self.yPos += deltaY
				game.entities[self.yPos][self.xPos].append(self)
				game.entity_icons[self.yPos][self.xPos].append(self.icon)
				for i in game.entities[self.yPos][self.xPos]:
					if i != game.player:
						print(game.entities[self.yPos][self.xPos])
						if not len(game.entities[self.yPos][self.xPos]) > 3:
							game.say("You see here a " + game.entities[self.yPos][self.xPos][0].description + " " + game.entities[self.yPos][self.xPos][0].name)
						else:
							game.say("You see here several items")
			except IndexError:
				self.xPos -= deltaX
				self.yPos -= deltaY
				game.entities[self.yPos][self.xPos] = game.player
				game.entity_icons[self.yPos][self.xPos] = game.player.icon

		if can_whack:
			print(game.player)
			print(game)
			thing = game.entities[self.yPos + deltaY][self.xPos + deltaX][0]
			print(thing)
			game.player.attack(thing, 10)



class Book(Entity):

	def __init__(self, description):
		super(Book, self).__init__()
		self.description = description
		self.name = "book"
		self.icon = "B"


class NullEntity(Entity):

	def __init__(self):
		self.icon = " "