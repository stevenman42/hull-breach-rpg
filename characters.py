
class Character(object):
	def __init__(self, speed, armor, health):
		self.speed = speed
		self.armor = armor
		self.health = health



class Knight(Character):
	"""docstring for Knight"""
	def __init__(self):
		super(Knight, self).__init__(3, 8, 6)

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self):
		print("created a wizard")
		super(Wizard, self).__init__(5, 3, 8)



