import random, os
import inventory
import input as key_input

getch = key_input._GetchUnix()

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
			elif i.whackable == False:
				can_whack = False

		if can_move:
			game.render()
			try:
				game.remove_entity(self.xPos, self.yPos, self)
				self.xPos += deltaX
				self.yPos += deltaY
				game.add_entity(self.xPos, self.yPos, self)
				for i in game.entities[self.yPos][self.xPos]:
					if i != game.player:
						# len(game.entities[self.yPos][self.xPos]) is the number of entities that are on the tile that "self" is standing on
						if len(game.entities[self.yPos][self.xPos]) == 2:
							game.say("You see here a " + game.entities[self.yPos][self.xPos][0].description + " " + game.entities[self.yPos][self.xPos][0].name)
						if len(game.entities[self.yPos][self.xPos]) == 3:
							game.say("You see here a " + game.entities[self.yPos][self.xPos][0].description + " " + game.entities[self.yPos][self.xPos][0].name)
							game.say("You also see a " + game.entities[self.yPos][self.xPos][1].description + " " + game.entities[self.yPos][self.xPos][1].name)
							break
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
			thing = game.entities[self.yPos + deltaY][self.xPos + deltaX][-1]
			print(thing)
			game.player.attack(thing, game.player.damage + random.randint(-2,2))


	def tick(self, game):
		pass

class Chest(Entity):
	"""This is an example of why an entity that's not a player or a monster would need an inventory"""
	def __init__(self, items, description):
		self.inventory = inventory.Inventory([])
		self.description = description
		self.icon = "C"
		self.walkable = True
		self.whackable = False
		self.name = "chest"
		for item in items:
			self.inventory.add_item(item)

	def apply(self, game):
		if len(self.inventory.items) < 1:
			game.say("There's nothing in this chest")
			game.render()
		else:
			os.system("clear")
			print("")
			print("         What do you want to take from the " + self.description + " Chest")
			print("_" * 30)
			print("|" + " " * 28 + "|")
			for i in range(len(self.inventory.items)):
				item_len = len("| " + str(i + 1) + ":  " + self.inventory.items[i].description + " " + self.inventory.items[i].name + "   |")
				padding = int((32 - item_len) / 2)
				print("| " + " " * padding + str(i + 1) + ":  " + self.inventory.items[i].description + " " + self.inventory.items[i].name + " " * (padding - 2) + "   |")
			print("|" + "_" * 28 + "|")
			inn = None
			while inn == None:
				inn = getch.__call__()
			if inn in "1234567890":
				game.player.inventory.add_item(self.inventory.items[int(inn) - 1])
				self.inventory.remove_item(self.inventory.items[int(inn) - 1])
			else:
				print(inn)

class Book(Entity):

	def __init__(self, description, xPos=None, yPos=None):
		super(Book, self).__init__(xPos, yPos)
		self.description = description
		self.name = "book"
		self.icon = "B"

	def apply(self, game):
		game.say('You read the ' + self.description + ' book')


class NullEntity(Entity):
	# what the heck is a null entity

	def __init__(self, xPos, yPos):
		super(NullEntity, self).__init__(xPos, yPos)
		self.icon = " "

class WallEntity(Entity):

	def __init__(self, type, xPos, yPos):
		super(WallEntity, self).__init__(xPos, yPos)
		self.icon = "#"
		self.type = type
		self.walkable = False