import entities
import random
import inventory

class Monster(entities.Entity):
	def __init__(self, speed, armor, health, damage, icon, xPos, yPos):
		super(Monster, self).__init__(xPos, yPos)
		self.speed = speed
		self.armor = armor
		self.health = health
		self.damage = damage
		self.icon = icon
		self.whackable = True
		self.type = "Monster"

	def die(self, game):
		game.remove_entity(self.xPos, self.yPos, self)
		for item in self.inventory.items:
			item.drop(self, game, item)
		print("MONSTER DIED RIP IN KIL")
		
	def attack(self,target,damage):
		self.game.say("The " + self.name + " attacks for " + str(damage) + " damage")
		target.health -= damage

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

			game.remove_entity(self.xPos, self.yPos, self)
			self.xPos += deltaX
			self.yPos += deltaY
			print(str(self.xPos) + " " + str(self.yPos))
			game.add_entity(self.xPos, self.yPos, self)

		if can_whack and not(self.type == "Monster" and game.entities[self.yPos + deltaY][self.xPos + deltaX][-1].type == "Monster"):
			self.attack(game.entities[self.yPos + deltaY][self.xPos + deltaX][-1], 5)

	def tick(self, game):
		rand = random.randint(0, 1)
		self.game = game

		# the random numbers are so that their movement isn't just straight up and straight over
		# however it's also kind of broken but idk if it has to do with this bit
		# but it needs to be fixed
		# hopefully it'll work itself out when I work on pathfinding
		# yeah right
		if rand == 1:
			if game.player.xPos > self.xPos:
				self.move(game, 1, 0)
				return
			elif game.player.xPos < self.xPos:
				self.move(game, -1, 0)
				return

			if game.player.yPos > self.yPos:
				self.move(game, 0, 1)
				return
			elif game.player.yPos < self.yPos:
				self.move(game, 0, -1)
				return

		elif rand == 0:

			if game.player.yPos > self.yPos:
				self.move(game, 0, 1)
				return
			elif game.player.yPos < self.yPos:
				self.move(game, 0, -1)
				return
			if game.player.xPos > self.xPos:
				self.move(game, 1, 0)
				return
			elif game.player.xPos < self.xPos:
				self.move(game, -1, 0)
				return



class Orc(Monster):
	"""docstring for Orc"""
	def __init__(self, xPos, yPos):
		print("created an Orc")
		speed = 7
		armor = 3
		health = 40
		damage = 4
		icon = 'o'
		super(Orc, self).__init__(speed, armor, health, damage, icon, xPos, yPos)
		self.walkable = False
		self.name = "Orc"
		self.inventory = inventory.Inventory([entities.Book("Kinda okay")])

class Monkey(Monster):
	"""docstring for Monkey"""
	def __init__(self, xPos, yPos):
		print("created a Monkey")
		speed = 5
		armor = 3
		health = 40
		damage = 5
		icon = 'm'
		super(Monkey, self).__init__(speed, armor, health, damage, icon, xPos, yPos)
		self.walkable = False
		self.name = "Monkey"
		self.inventory = inventory.Inventory([entities.Book("Monkey")])

class Dragon(Monster):
	"""docstring for Dragon"""
	def __init__(self, xPos, yPos):
		print("created a Dragon")
		speed = 3
		armor = 7
		health = 10
		damage = 7
		icon = 'D'
		super(Dragon, self).__init__(speed, armor, health, damage, icon, xPos, yPos)
		self.walkable = False
		self.name = "Dragon"



class Pig(Monster):
	"""docstring for Pig"""
	def __init__(self, xPos, yPos):
		print("created a Pig")
		speed = 5
		armor = 3
		health = 40
		damage = 7
		icon = 'p'
		super(Pig, self).__init__(speed, armor, health, damage, icon, xPos, yPos)
		self.walkable = False
		self.name = "Pig"
		self.inventory = inventory.Inventory([entities.Book("Poggerchump")])