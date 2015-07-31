import entities

class Character(entities.Entity):
	def __init__(self, game, speed, armor, health, damage, hunger, xPos=0, yPos=0):
		self.game = game
		self.speed = speed
		self.armor = armor
		self.health = health
		self.damage = damage
		self.xPos = xPos
		self.yPos = yPos
		self.level = 0

		self.inventory = []

		self.icon = "0"
		self.walkable = False
		self.whackable = True

	def attack(self,target,damage):
		target.health -= damage
		print("u dun it")
		self.game.say("You whack the " + target.name)

	def pick_up(self, item):
		self.inventory.append(item.name)
		self.game.remove_entity(self.xPos, self.yPos, item)



class Knight(Character):
	"""docstring for Knight"""
	def __init__(self, game):
		print("created a Knight")
		super(Knight, self).__init__(game, 3, 8, 6, 5, 10)

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self, game):
		print("created a wizard")
		super(Wizard, self).__init__(game, 5, 3, 8, 7, 10)

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self, game):
		print("created a Gunner")
		super(GunDude, self).__init__(game, 6, 5, 5, 8, 10)

class Rogue(Character):
	"""docstring for Wizard"""
	def __init__(self, game):
		print("created a Rogue")
		super(Roag, self).__init__(game, 10, 5, 8, 2, 10)

