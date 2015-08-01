import entities
import random

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
			game.add_entity(self.xPos, self.yPos, self)
			#game.entity_icons[self.yPos][self.xPos].append(self.icon)

		if can_whack:
			self.attack(game.entities[self.yPos + deltaY][self.xPos + deltaX][-1], 5)

	def tick(self, game):
		rand = random.randint(0, 1)
		self.game = game

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
		super(Orc, self).__init__(7, 3, 40, 4, 'o', xPos, yPos)
		self.walkable = False
		self.name = "Orc"

class Monkey(Monster):
	"""docstring for Monkey"""
	def __init__(self, xPos, yPos):
		print("created a Monkey")
		super(Monkey, self).__init__(5, 3, 4, 5, 'm', xPos, yPos)
		self.walkable = False
		self.name = "Monkey"

class Dragon(Monster):
	"""docstring for Dragon"""
	def __init__(self, xPos, yPos):
		print("created a Dragon")
		super(Dragon, self).__init__(3, 7, 10, 7, 'D', xPos, yPos)
		self.walkable = False
		self.name = "Dragon"