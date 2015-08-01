import entities
import inventory

class Character(entities.Entity):
	def __init__(self, game, speed, armor, health, damage, hunger, strength, xPos=0, yPos=0):
		self.game = game
		self.speed = speed
		self.armor = armor
		self.health = health
		self.damage = damage
		self.xPos = xPos
		self.yPos = yPos
		self.level = 0



		self.icon = "0"
		self.walkable = False
		self.whackable = True

	def attack(self,target,damage):
		target.health -= damage
		self.game.say("You whack the " + target.name + " for " + str(damage) + " damage")

	def pick_up(self, item):
		self.inventory.add_item(item)
		self.game.remove_entity(self.xPos, self.yPos, item)



class Knight(Character):
	"""docstring for Knight"""
	def __init__(self, game, xPos, yPos):
		print("created a Knight")
		super(Knight, self).__init__(game, 3, 8, 60, 15, 10, 2, xPos, yPos)
		self.inventory = inventory.Inventory(entities.Book("Great"))

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self, game, xPos, yPos):
		print("created a wizard")
		super(Wizard, self).__init__(game, 5, 3, 8, 7, 1, 10)
		self.inventory = inventory.Inventory("Wand")

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self, game, xPos, yPos):
		print("created a Gunner")
		super(Gunner, self).__init__(game, 6, 5, 5, 8, 1, 10)
		self.inventory = inventory.Inventory("Gun")

class Rogue(Character):
	"""docstring for Wizard"""
	def __init__(self, game, xPos, yPos):
		print("created a Rogue")
		super(Rogue, self).__init__(game, 10, 5, 8, 2, 0, 10)
		self.inventory = inventory.Inventory("Knife")

