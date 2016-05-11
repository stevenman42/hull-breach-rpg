import os, sys, random, time, string
import input as key_input
import characters
import info
import entities
import monsters
import console
import json

# Writing JSON data
def save_settings(data):
	data = ['a', 't', 'd', ',', ' ', 'up', 'down', 'left', 'right', 'q', 'i']
	with open('settings.json', 'w') as f:
	     json.dump(data, f)

# Reading data back
def load_settings():
	with open('settings.json', 'r') as f:
	     data = json.load(f)
	return data


# the doodad that gets the keyboard input
getch = key_input._GetchUnix()


# for i in range(10):
#     print(getch.__call__())
    #getch.__call__()



class Game(object):
	"""
	Contains information about the character that the player chose, the map, and the entities within the map
	"""
	def __init__(self, Character, width=10, height=10, playerX=5, playerY=5):

		self.player = Character
		self.map = []

		# entities, and entity_icons are matrices that are the same size as the map matrix,
		# but they contain stuff like items and the player (the entity matrix) and the icons
		# that go with them (the entity_icons matrix)
		self.entities = []
		self.entity_icons = []
		self.info = info.Info(self.player)
		self.entity_array = []

		self.time = 0

		# this is probably temporary code I think
		for i in range(height):
			self.map.append([])
			self.entities.append([])
			self.entity_icons.append([])
			for j in range(width):
				self.map[i].append(".")

				if i == 0 or i == height - 1 or j == width - 1 or j == 0:
					self.entities[i].append([entities.WallEntity("unbreakable", j, i)])
					self.entity_icons[i].append(["#"])
				else:
					self.entities[i].append([])
					self.entity_icons[i].append([])



		self.height = len(self.map)
		self.width = len(self.map[0])


		self.add_entity(1, 1, self.player)

		# TEST CODE PLS IGNORE
		self.add_entity(5, 5, entities.Book("Super red", 5, 5))
		self.add_entity(5, 5, entities.Book("Swell", 5, 5))
		self.add_entity(5, 5, entities.Book("Greasy", 5, 5))
		self.add_entity(4, 9, entities.Book("Plaid", 4, 9))
		# self.add_entity(20, 4, monsters.Orc(20, 4))
		# self.add_entity(20, 5, monsters.Monkey(20, 5))
		self.add_entity(20, 6, monsters.Pig(20, 6))
		self.add_entity(1, 5, entities.Chest([entities.Book("The")], "Regular"))
		self.add_entity(10,10, entities.Sword("Shiny"))
		self.add_entity(11,11, entities.Egg("Boiled"))


		self.say("Welcome to hull breach!  Watch out for hull breaches!")
		self.say("""3 years ago, you retired from your job as a """ + self.player.title.lower() + """.  After a period of homelessness, you find yourself working on a submarine off the coast of Siberia as a result of a brush with the Russian mafia.  The submarine you work on contains experiments involving the genetic mutation of animals.  Everything was going swell, until one day, after a lazy technician forgot to make his inspection of the hull, there was a breach, and now the cold Siberian sea is leaking into the submarine.  Now the sub is engulfed in chaos, so it is up to you to navigate through the rooms of the submarine and find the hull breach and patch it before it's too late.""")
		self.render()
		

	def add_entity(self, xPos, yPos, entity):
		self.entities[yPos][xPos].append(entity)
		self.entity_icons[yPos][xPos].append(entity.icon)
		self.entity_array.append(entity)

	def remove_entity(self, xPos, yPos, entity):
		self.entities[yPos][xPos].remove(entity)
		self.entity_icons[yPos][xPos].remove(entity.icon)
		self.entity_array.remove(entity)

	def get_entity(self, xPos, yPos, zPos):
		try:
			return self.entities[yPos][xPos][zPos]
		except IndexError:
			return entities.NullEntity(xPos, yPos)

	def get_entity_icon(self, xPos, yPos, zPos):
		try:
			return self.get_entity(xPos, yPos, zPos).icon
		except IndexError:
			return " "
		
	def render(self):
		os.system("clear")
		(width, height) = console.getTerminalSize()

		self.info.render()
		self.info.render_dialogue()

		horiz_buffer = " " * int((width - self.width) / 2)


		# draws everything in the map array, and everything in the entity_icons array
		for i in range(self.height):
			sys.stdout.write(horiz_buffer)
			for j in range(self.width):
				try:
					if self.entity_icons[i][j][-1] == " ":
						sys.stdout.write(self.map[i][j])

					elif self.entity_icons[i][j][-1] != " ":
						# always uses the last item in the list for rendering
						try:
							sys.stdout.write(self.entity_icons[i][j][-1])
						except IndexError:
							pass
				except IndexError:
					sys.stdout.write(".")

			if i == self.height - 1:
				print("    " + str(self.time))

			sys.stdout.write("\n")


	def render_inventory(self, msg=""):
		os.system("clear")
		print("")
		if msg != "":
			print(msg)
		print("          Inventory")
		print("_" * 30)
		print("|" + " " * 28 + "|")
		for i in range(len(self.player.inventory.items)):
			item_len = len("| " + str(i + 1) + ":  " + self.player.inventory.items[i].description + " " + self.player.inventory.items[i].name + "   |")
			padding = int((32 - item_len) / 2)
			print("| " + " " * padding + str(i + 1) + ":  " + self.player.inventory.items[i].description + " " + self.player.inventory.items[i].name + " " * (padding - 2) + "   |")
		print("|" + "_" * 28 + "|")

	def say(self, dialogue):
		self.info.add_dialogue(dialogue)

	def hull_breach(self):
		os.system("clear")
		print("OH NO")
		time.sleep(1)
		print("IT'S A...")
		time.sleep(2)
		print(" _   _ _   _ _     _       ____  ____  _____    _    ____ _   _ ")
		print("| | | | | | | |   | |     | __ )|  _ \| ____|  / \  / ___| | | |")
		print("| |_| | | | | |   | |     |  _ \| |_) |  _|   / _ \| |   | |_| |")
		print("|  _  | |_| | |___| |___  | |_) |  _ <| |___ / ___ \ |___|  _  |")
		print("|_| |_|\___/|_____|_____| |____/|_| \_\_____/_/   \_\____|_| |_|")
		for i in range(5):
			time.sleep(.5)
			os.system("clear")
			print("OH NO")
			print("IT'S A...")
			time.sleep(.5)
			print(" _   _ _   _ _     _       ____  ____  _____    _    ____ _   _ ")
			print("| | | | | | | |   | |     | __ )|  _ \| ____|  / \  / ___| | | |")
			print("| |_| | | | | |   | |     |  _ \| |_) |  _|   / _ \| |   | |_| |")
			print("|  _  | |_| | |___| |___  | |_) |  _ <| |___ / ___ \ |___|  _  |")
			print("|_| |_|\___/|_____|_____| |____/|_| \_\_____/_/   \_\____|_| |_|")

		self.tick()

	def tick(self):

		# checks to make sure nothing is still sticking around after is has 0 or less health
		# this should probably not be here
		for row in self.entities:
			for col in row:
				for thingy in col:
					try:
						if thingy.health <= 0:
							#self.remove_entity(thingy.xPos, thingy.yPos, thingy)
							thingy.die(self)
							kill_adj = ["brutally", "efficiently", "swiftly", "messily", "violently", "cheerfully"][random.randint(0,5)]
							kill_msg = ["murder", "slaughter", "destroy", "annihilate", "obliterate", "kill", "massacre"][random.randint(0,6)]
							self.say("You " + kill_adj + " " + kill_msg + " the " + thingy.name)
					except AttributeError:
						# this occurs when the entity doesn't have any health, like a book or other item
						pass
					#thingy.tick(self)


		for entity in self.entity_array:
			entity.tick(self)

		if self.player.health <= 0:
			self.say("ur ded rip in piece")
			self.remove_entity(self.player.xPos, self.player.yPos, self.player)
			self.render()
			sys.exit()

		self.time += 1

		if self.time % 5 == 0:
			self.player.hunger -= 1

		self.render()

		if random.randint(1, 1000) == 1:
			self.hull_breach()

def run(guy):
	game = Game(guy, 70, 20, 5, 5)
	guy.game = game

	inv = False

	# here's where the controls are defined 
	# arrow keys - move
	# a - use/apply
	# t - throw item
	# d - drop item
	# , - pick up
	# q - quit
	# i - inventory
	# space - wait

	while 1:
		inn = getch.__call__()
		if inn == "j":
			game.info.scroll_back()
			game.render()
		elif inn == "k":
			game.info.scroll_forward()
			game.render()
		if inn in game.player.controls.keys():
			# if the function needs to not tick, make it return something
			if game.player.controls[inn](game) == None:
				game.tick()

		else:
			# print(inn)
			pass


