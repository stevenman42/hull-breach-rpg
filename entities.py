import random, os
import inventory
import input as key_input

getch = key_input._GetchUnix()

# pretty sure that everywhere the game object is passed to a function it could be replaced by having a field in the Entity class, but that's none of my business

class Entity(object):
	"""This is the thing that everything is pretty much except for the stuff that isn't this"""
	# nice
	def __init__(self, xPos, yPos):
		self.walkable = True
		self.whackable = False
		self.xPos = xPos
		self.yPos = yPos

		# how much damage the item causes when used as a weapon
		self.damage = 1

	def equip(self):
		return False

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

			thing = game.entities[self.yPos + deltaY][self.xPos + deltaX][-1]
			game.player.attack(thing, game.player.damage + random.randint(-2,2))


	def tick(self, game):
		pass


class RangedWeapon(Entity):
	def __init__(self, description, range, xPos=None, yPos=None):
		super(RangedWeapon, self).__init__(xPos, yPos)
		self.description = description
		self.range = range
		self.icon = ">"

	def apply(self, game):
		if game.player.inventory.equips[4] != 0 and game.player.inventory.equips[4].name == self.name:
			inn = None
			game.say("In what direction do you want to fire the " + self.name.lower() + "?")
			game.render()
			while inn not in ["up", "down", "left", "right"]:
				deltaY, deltaX, can_whack = 0,0,False
				inn = getch.__call__()

				if inn == "up":
					deltaY = -1
				elif inn == "down":
					deltaY = 1
				elif inn == "left":
					deltaX = -1
				elif inn == "right":
					deltaY = 1

				for i in game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX]:
					if i.whackable == True:
						can_whack = True
					elif i.whackable == False:
						can_whack = False

				if not can_whack:
					try:
						game.say("You hit the " + game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX][0].name + " to no avail.")
					except IndexError:
						game.say("The " + self.name.lower() + " swishes as you swing it wildly at the air.")
				else:
					try:
						game.player.attack(game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX][0], game.player.damage + self.damage)
					except IndexError:
						game.player.attack(game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX], game.player.damage + self.damage)
		else:
			game.say("You don't have that equipped.")


class MeleeWeapon(Entity):
	def __init__(self, description, xPos=None, yPos=None):
		super(MeleeWeapon, self).__init__(xPos, yPos)
		self.description = description
		self.icon = "^"

	def apply(self, game):
		if game.player.inventory.equips[4] != 0 and game.player.inventory.equips[4].name == self.name:
			inn = None
			game.say("In what direction do you want to swing the " + self.name.lower() + "?")
			game.render()
			while inn not in ["up", "down", "left", "right"]:
				deltaY, deltaX, can_whack = 0,0,False
				inn = getch.__call__()

				if inn == "up":
					deltaY = -1
				elif inn == "down":
					deltaY = 1
				elif inn == "left":
					deltaX = -1
				elif inn == "right":
					deltaY = 1

				for i in game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX]:
					if i.whackable == True:
						can_whack = True
					elif i.whackable == False:
						can_whack = False

				if not can_whack:
					try:
						game.say("You hit the " + game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX][0].name + " to no avail.")
					except IndexError:
						game.say("The " + self.name.lower() + " swishes as you swing it wildly at the air.")
				else:
					try:
						game.player.attack(game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX][0], game.player.damage + self.damage)
					except IndexError:
						game.player.attack(game.entities[game.player.yPos + deltaY][game.player.xPos + deltaX], game.player.damage + self.damage)
		else:
			game.say("You don't have that equipped.")

	def equip(self, game):
		# game.say('You equip the ' + self.description + ' sword')
		a = game.player.inventory.equip_item(self, 4)
		if a != False:
			game.say(a)
		else:
			pass


class Food(Entity):
	"""I would make this docstring if I was a good programmer"""
	def __init__(self, description, xPos=None, yPos=None):
		super(Food, self).__init__(xPos, yPos)
		self.description = description
		self.satiation = 0

	def apply(self, game):
		game.player.eat(self, self.satiation)

class Egg(Food):
	def __init__(self, description, xPos=None, yPos=None):
		super(Egg, self).__init__(xPos, yPos)
		self.description = description
		self.satiation = 10
		self.icon = 'o'
		self.name = "egg"


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



class Sword(MeleeWeapon):
	def __init__(self, description, xPos=None, yPos=None):
		super(Sword, self).__init__(xPos, yPos)
		self.description = description
		self.name = "Sword"
		self.icon = "^"


class Gun(RangedWeapon):
	def __init__(self, description, xPos=None, yPos=None):
		super(Sword, self).__init__(xPos, yPos)
		self.description = description
		self.name = "Sword"
		self.icon = "^"
		self.damage = 10


class Book(Entity):

	def __init__(self, description, xPos=None, yPos=None):
		super(Book, self).__init__(xPos, yPos)
		self.description = description
		self.name = "book"
		self.icon = "B"
		self.whackable = False

	def apply(self, game):
		game.say('You read the ' + self.description + ' book')


class NullEntity(Entity):
	# what the heck is a null entity

	def __init__(self, xPos, yPos):
		super(NullEntity, self).__init__(xPos, yPos)
		self.icon = " "
		self.name = "NULL"

class WallEntity(Entity):

	def __init__(self, type, xPos, yPos):
		super(WallEntity, self).__init__(xPos, yPos)
		self.icon = "#"
		self.type = type
		self.walkable = False
		self.name = "wall"