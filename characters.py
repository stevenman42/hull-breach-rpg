
class Character(object):
	def __init__(self, speed, armor, health, attack, hunger):
		self.speed = speed
		self.armor = armor
		self.health = health
		self.attack = attack

	def attack(self,object,damage):
		object.health -= damage


class Knight(Character):
	"""docstring for Knight"""
	def __init__(self):
		print("created a Knight")
		super(Knight, self).__init__(3, 8, 6, 5, 10)

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self):
		print("created a wizard")
		super(Wizard, self).__init__(5, 3, 8, 7, 10)

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self):
		print("created a Gunner")
		super(GunDude, self).__init__(6, 5, 5, 8, 10)

class Rogue(Character):
	"""docstring for Wizard"""
	def __init__(self):
		print("created a Rogue")
		super(Roag, self).__init__(10, 5, 8, 2, 10)

