import entities
import inventory
import input as key_input
import random
import string

getch = key_input._GetchUnix()

class MonsterOrPlayer(entities.Entity):
	def __init__(self, game, speed, armor, health, damage, strength, xPos=0, yPos=0):
		super(MonsterOrPlayer, self).__init__(xPos, yPos)
		self.speed = speed
		self.armor = armor
		self.health = health
		self.damage = damage
		self.strength = strength




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
		self.hunger = hunger
		self.strength = strength
		self.xPos = xPos
		self.yPos = yPos
		self.level = 0
		self.inv = False

		self.type = "Character"


		self.icon = "0"
		self.walkable = False
		self.whackable = True

		self.controls = {"a": self.apply, "t": self.throw, "d": self.drop, ",": self.pickup, " ": self.wait, "up": self.move_up, "down": self.move_down, "left": self.move_left, "right": self.move_right, "q": self.quit, "i": self.show_inventory}

	def attack(self,target,damage):
		damage -= target.armor
		target.health -= damage
		self.game.say("You whack the " + target.name + " for " + str(damage) + " damage")

	def pick_up(self, item):
		self.inventory.add_item(item)
		self.game.remove_entity(self.xPos, self.yPos, item)

	def apply(self, game):
		if len(game.player.inventory.items) <= 0:
			game.say("You ain't got nothin' to use or apply!")
			game.render()

		else:
			#inn = getch.__call__()
			game.render_inventory("What do you want to use or apply?")
			inn = False
			while inn == False:
				inn = getch.__call__()
				game.render_inventory("What do you want to use or apply?")
			if inn in "1234567890":
				try:
					game.player.inventory.items[int(inn) - 1].apply(game)
					game.render()
				except AttributeError:
					game.say("You can't use that, silly rabbit!")
					game.render()
			else:
				game.say("you don't have that, silly")
				game.render()

	def pickup(self, game):
		if game.get_entity_icon(game.player.xPos, game.player.yPos, -2) != "0" and game.get_entity_icon(game.player.xPos, game.player.yPos, -2) != " ":
			game.say("you picked up the " + game.get_entity(game.player.xPos, game.player.yPos, -2).description + " " + game.get_entity(game.player.xPos, game.player.yPos, -2).name)
			game.player.pick_up(game.get_entity(game.player.xPos, game.player.yPos, -2))
			game.render()

	def throw(self, game):

		if len(game.player.inventory.items) <= 0:
			game.say("You ain't got nothin' to throw!")
			game.render()

		else:
			# this bit should probably be written into its own method
			# note: the drop method could be used, because you can set the xPos and yPos of where the item is dropped
			# this is not well written

			game.render_inventory("What do you want to throw?")
			inn = False
			while inn == False:
				inn = getch.__call__()
				game.render_inventory("What do you want to throw?")
			if not inn in "1234567890":
				game.say("You don't have that item, silly goose!")
			else:
				num = int(inn) - 1
				dum = None
				while dum == None:
					game.say("What direction do you want to throw the " + game.player.inventory.items[num].description + " " + game.player.inventory.items[num].name + "?")
					game.render()
					dum = getch.__call__()

					if dum == "up":

						try:
							variance = random.randint(-1, 2)
							if not (game.player.yPos - game.player.strength * 3 - variance) < 1:
								game.add_entity(game.player.xPos, game.player.yPos - game.player.strength * 3 - variance, game.player.inventory.items[num])
							else:
								# this bit is literally just put in to throw an error
								stupid = []
								print(stupid[1])
						except IndexError:

							temp_list = range(game.player.yPos + game.player.strength * 3 + variance)
							temp_list.reverse()
							for i in temp_list:
								#game.say("HERE'S THE NUMBER " + str(game.player.yPos - game.player.strength * 3 - variance + i))
								game.render()
								if not (game.player.yPos - i) < 1:
									try:
										game.add_entity(game.player.xPos, game.player.yPos - i, game.player.inventory.items[num])
										break
									except IndexError:
										pass
								else:
									pass
									#game.add_entity(game.player.xPos, 1)
						game.player.inventory.remove_item(game.player.inventory.items[num])
						game.render()


					if dum == "down":
						try:
							variance = random.randint(-1, 2)
							if not (game.player.yPos + game.player.strength * 3 + variance) >= game.height - 1:
								game.add_entity(game.player.xPos, game.player.yPos + game.player.strength * 3 + variance, game.player.inventory.items[num])
							else:
								# see above if this confuses you
								stupid = []
								print(stupid[1])
						except IndexError:

							temp_list = range(game.player.yPos + game.player.strength * 3 + variance)
							temp_list.reverse()
							for i in temp_list:
								if not (game.player.yPos + i) >= game.height - 1:
									try:
										game.add_entity(game.player.xPos, game.player.yPos + i, game.player.inventory.items[num])
										break
									except IndexError:
										pass
								else:
									pass
						game.player.inventory.remove_item(game.player.inventory.items[num])
						game.render()


					if dum == "left":
						try:
							variance = random.randint(-1, 2)
							if not (game.player.xPos - game.player.strength * 3 - variance) < 1:
								game.add_entity(game.player.xPos - game.player.strength * 3 - variance, game.player.yPos, game.player.inventory.items[num])
							else:
								stupid = []
								print(stupid[1])
						except IndexError:

							temp_list = range(game.player.yPos + game.player.strength * 3 + variance)
							temp_list.reverse()
							for i in temp_list:
								if not (game.player.xPos - i) < 1:
									try:
										game.add_entity(game.player.xPos - i, game.player.yPos, game.player.inventory.items[num])
										break
									except IndexError:
										pass
								else:
									pass
						game.player.inventory.remove_item(game.player.inventory.items[num])
						game.render()


					if dum == "right":
						try:
							variance = random.randint(-1, 2)
							if not (game.player.xPos + game.player.strength * 3 - variance) < 1:
								game.add_entity(game.player.xPos + game.player.strength * 3 + variance, game.player.yPos, game.player.inventory.items[num])
							else:
								stupid = []
								print(stupid[1])
						except IndexError:

							temp_list = range(game.player.xPos + game.player.strength * 3 + variance)
							temp_list.reverse()
							for i in temp_list:
								if not (game.player.xPos + i) >= game.width - 1:
									try:
										game.add_entity(game.player.xPos + i, game.player.yPos, game.player.inventory.items[num])
										break
									except IndexError:
										pass
								else:
									pass
						game.player.inventory.remove_item(game.player.inventory.items[num])
						game.render()

	def drop(self, game):

		game.render_inventory("What do you want to drop?")
		inn = False
		while inn == False:
			inn = getch.__call__()



		if inn in string.lowercase + "1234567890":
			try:
				game.say("You drop a " + game.player.inventory.items[int(inn) - 1].description + " " + game.player.inventory.items[int(inn) - 1].name)
				game.render()
				super(Character, self).drop(game.player, game, game.player.inventory.items[int(inn) - 1])
			except IndexError:
				game.say("You don't have that item, silly!")
				game.render()
		else:
			game.say("You don't have that item, silly!")
			game.render()

	def wait(self, game):
		game.tick()

	def move_up(self, game):
		super(Character, self).move(game, 0, -1)

	def move_down(self, game):
		super(Character, self).move(game, 0, 1)

	def move_left(self, game):
		super(Character, self).move(game, -1, 0)

	def move_right(self, game):
		super(Character, self).move(game, 1, 0)

	def quit(self, game):
		os.system("clear")
		print("bai")
		sys.exit()

	def show_inventory(self, game):
		if not self.inv:
			game.render_inventory()
			self.inv = not self.inv
		else:
			game.tick()
			self.inv = not self.inv
		return False


	# def apply(self, item, game):
	# 	game.say("This function has not been defined yet")



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
		self.inventory = inventory.Inventory([entities.Book("Great")])
		self.title = "Knight"

class Wizard(Character):
	"""docstring for Wizard"""
	def __init__(self, name, game, xPos, yPos):

		speed = 3
		armor = 8
		health = 60
		damage = 15
		hunger = 10
		strength = 2


		super(Wizard, self).__init__(name, game, 5, 3, 8, 7, 1, 10)
		self.inventory = inventory.Inventory("Wand")
		self.title = "Wizard"

class Gunner(Character):
	"""docstring for Gunner"""
	def __init__(self, name, game, xPos, yPos):

		speed = 3
		armor = 8
		health = 60
		damage = 15
		hunger = 10
		strength = 2


		super(Gunner, self).__init__(name, game, 6, 5, 5, 8, 1, 10)
		self.inventory = inventory.Inventory("Gun")
		self.title = "Gunner"

class Rogue(Character):
	"""docstring for Wizard"""
	def __init__(self, name, game, xPos, yPos):

		speed = 3
		armor = 8
		health = 60
		damage = 15
		hunger = 10
		strength = 2


		super(Rogue, self).__init__(name, game, 10, 5, 8, 2, 0, 10)
		self.inventory = inventory.Inventory("Knife")
		self.title = "Rogue"

