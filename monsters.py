import entities

class Monster(entities.Entity):
	def __init__(self, speed, armor, health, attack, icon):
		self.speed = speed
		self.armor = armor
		self.health = health
		self.attack = attack

	def attack(self,object,damage):
		object.health -= damage

	def move(self, game, deltaX, deltaY):
		print("movin'")
		#game.map[self.yPos][self.xPos] = "."
		game.entities[self.yPos][self.xPos] = None
		game.entity_tiles[self.yPos][self.xPos] = " "
		self.xPos += deltaX
		self.yPos += deltaY
		game.entities[self.yPos][self.xPos] = game.player
		game.entity_tiles[self.yPos][self.xPos] = game.player.icon

class Orc(Monster):
	"""docstring for Orc"""
	def __init__(self):
		print("created an Orc")
		super(Orc, self).__init__(7, 3, 2, 4, 'o')

class Monkey(Monster):
	"""docstring for Monkey"""
	def __init__(self):
		print("created a Monkey")
		super(Monkey, self).__init__(5, 3, 4, 5, 'm')

class Dragon(Monster):
	"""docstring for Dragon"""
	def __init__(self):
		print("created a Dragon")
		super(Dragon, self).__init__(3, 7, 10, 7, 'D')