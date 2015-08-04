import random

class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	def __init__(self, xPos, yPos):
		self.walkable = True
		self.whackable = False
		self.xPos = xPos
		self.yPos = yPos

	def drop(self, holder, game, item):
		holder.inventory.remove_item(item)
		game.add_entity(holder.xPos, holder.yPos, item)
		game.say("The " + str(self) + " is dropped")


	def move(self, game, deltaX, deltaY):

		can_move = True
		can_whack = False

		print(game.entities[self.yPos + deltaY][self.xPos + deltaX])
		for i in game.entities[self.yPos + deltaY][self.xPos + deltaX]:
			if i.walkable == False:
				can_move = False
			if i.whackable == True:
				can_move = False
				can_whack = True

		if can_move:
			game.render()
			try:
				game.remove_entity(self.xPos, self.yPos, self)
				self.xPos += deltaX
				self.yPos += deltaY
				game.add_entity(self.xPos, self.yPos, self)
				for i in game.entities[self.yPos][self.xPos]:
					if i != game.player:
						print(game.entities[self.yPos][self.xPos])
						if len(game.entities[self.yPos][self.xPos]) == 2:
							game.say("You see here a " + game.entities[self.yPos][self.xPos][0].description + " " + game.entities[self.yPos][self.xPos][0].name)
						if len(game.entities[self.yPos][self.xPos]) == 3:
							game.say("You see here a " + game.entities[self.yPos][self.xPos][0].description + " " + game.entities[self.yPos][self.xPos][0].name)
							game.say("You also see a " + game.entities[self.yPos][self.xPos][1].description + " " + game.entities[self.yPos][self.xPos][1].name)
						elif len(game.entities[self.yPos][self.xPos]) > 3:
							game.say("You see here several items")
							break
			except IndexError:
				self.xPos -= deltaX
				self.yPos -= deltaY
				game.add_entity(self.xPos, self.yPos, game.player)

		if can_whack:
			print(game.player)
			print(game)
			thing = game.entities[self.yPos + deltaY][self.xPos + deltaX][0]
			print(thing)
			game.player.attack(thing, game.player.damage + random.randint(-2,2))

	def tick(self, game):
		pass

class Chest(Entity):
	"""This isn't being implemented atm, but it's an example of why an entity that's not a player or a monster would need an inventory"""
	def __init__(self, items):
		for item in items:
			self.inventory.add_item(item)

class Book(Entity):

	def __init__(self, description, xPos=None, yPos=None):
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