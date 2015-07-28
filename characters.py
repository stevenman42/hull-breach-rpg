
class Character(object):
	def __init__(self, speed, armor, health, attack,hunger):
		self.speed = speed
		self.armor = armor
		self.health = health
		self.armor = attack

	def attack(self,object,damage):
		object.health -= damage

class Monster(object):
	def __init__(self, speed, armor, health, attack):
		self.speed = speed
		self.armor = armor
		self.health = health
		self.armor = attack

class Knight(Character):
	"""docstring for Knight"""
	def __init__(self):
		print("created a Knight")
		super(Knight, self).__init__(3, 8, 6, 5)

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self):
		print("created a wizard")
		super(Wizard, self).__init__(5, 3, 8, 7)

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self):
		print("created a Gunner")
		super(GunDude, self).__init__(6, 5, 5, 8)

class Roag(Character):
	"""docstring for Wizard"""
	def __init__(self):
		print("created a Roag")
		super(Roag, self).__init__(10, 5, 8, 2)

class Orc(Monster):
	"""docstring for Orc"""
	def __init__(self):
		print("created an Orc")
		super(Orc, self).__init__(7, 3, 2, 4)