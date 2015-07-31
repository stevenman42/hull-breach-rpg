class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	def __init__(self, xPos, yPos):
		self.walkable = True
		self.whackable = False
		self.xPos = xPos
		self.yPos = yPos


	def move(self, game, deltaX, deltaY):

		can_move = True
		can_whack = False

		print(game.entities[self.yPos + deltaY][self.xPos + deltaX])
		for i in game.entities[self.yPos + deltaY][self.xPos + deltaX]:
			print(i)
			if i.walkable == False:
				can_move = False
			if i.whackable == True:
				can_move = False
				can_whack = True

		if can_move:
			game.render()
			try:
				print("trying to remove the entity at " + str(self.xPos) + " and " + str(self.yPos))
				print(game.entities[self.xPos][self.yPos])
				game.remove_entity(self.xPos, self.yPos, self)
				self.xPos += deltaX
				self.yPos += deltaY
				game.add_entity(self.xPos, self.yPos, self)
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
				game.entities[self.yPos][self.xPos].append = game.player
				game.entity_icons[self.yPos][self.xPos].append = game.player.icon

		if can_whack:
			print(game.player)
			print(game)
			thing = game.entities[self.yPos + deltaY][self.xPos + deltaX][0]
			print(thing)
			game.player.attack(thing, 10)

	def tick(self, game):
		pass



class Book(Entity):

	def __init__(self, description, xPos, yPos):
		super(Book, self).__init__(xPos, yPos)
		self.description = description
		self.name = "book"
		self.icon = "B"


class NullEntity(Entity):

	def __init__(self, xPos, yPos):
		super(NullEntity, self).__init__(xPos, yPos)
		self.icon = " "

class WallEntity(Entity):

	def __init__(self, type, xPos, yPos):
		super(WallEntity, self).__init__(xPos, yPos)
		self.icon = "#"
		self.type = type
		self.walkable = False