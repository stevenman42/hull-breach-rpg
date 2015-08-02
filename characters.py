import entities
import inventory


# right now this is only used for the title sequence
# it's just a list of all the choices for characters
charlist = ["Knight", "Wizard", "Gunner", "Rogue"]

class Character(entities.Entity):
	def __init__(self, name, game, speed, armor, health, damage, hunger, strength, xPos=0, yPos=0):
		self.name = name
		self.game = game
		self.speed = speed
		self.armor = armor
		self.health = health
		self.damage = damage
		self.xPos = xPos
		self.yPos = yPos
		self.level = 0

		self.type = "Character"


		self.icon = "0"
		self.walkable = False
		self.whackable = True

	def attack(self,target,damage):
		damage -= target.armor
		target.health -= damage
		self.game.say("You whack the " + target.name + " for " + str(damage) + " damage")

	def pick_up(self, item):
		self.inventory.add_item(item)
		self.game.remove_entity(self.xPos, self.yPos, item)



class Knight(Character):
	"""docstring for Knight"""
	def __init__(self, name, game, xPos, yPos):

		speed = 3
		armor = 8
		health = 60
		damage = 15
		hunger = 10
		strength = 2

		super(Knight, self).__init__(name, game, speed, armor, health, damage, hunger, strength, xPos, yPos)
		self.inventory = inventory.Inventory(entities.Book("Great"))
		self.title = "Knight"

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self, name, game, xPos, yPos):

		super(Wizard, self).__init__(name, game, 5, 3, 8, 7, 1, 10)
		self.inventory = inventory.Inventory("Wand")
		self.title = "Wizard"

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self, name, game, xPos, yPos):

		super(Gunner, self).__init__(name, game, 6, 5, 5, 8, 1, 10)
		self.inventory = inventory.Inventory("Gun")
		self.title = "Gunner"

class Rogue(Character):
	"""docstring for Wizard"""
	def __init__(self, name, game, xPos, yPos):

		super(Rogue, self).__init__(name, game, 10, 5, 8, 2, 0, 10)
		self.inventory = inventory.Inventory("Knife")
		self.title = "Rogue"

