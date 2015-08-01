import os, sys, random
import input as key_input
import characters
import info
import entities
import monsters



# the doodad that gets the keyboard input
getch = key_input._GetchUnix()


# for i in range(10):
#     print(getch.__call__())
    #getch.__call__()



class Game(object):
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
		self.add_entity(20, 4, monsters.Orc(20, 4))
		self.add_entity(20, 5, monsters.Monkey(20, 5))


		self.say("Welcome to hull breach!  Watch out for hull breaches!")
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
			return entities.NullEntity()

	def get_entity_icon(self, xPos, yPos, zPos):
		try:
			return self.get_entity(xPos, yPos, zPos).icon
		except IndexError:
			return " "
		
	def render(self):
		os.system("clear")

		self.info.render()
		self.info.render_dialogue()

		for i in range(self.height):
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
		print()
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
		a = input("")
		print("IT'S A...")
		a = input("")
		print(" _   _ _   _ _     _       ____  ____  _____    _    ____ _   _ ")
		print("| | | | | | | |   | |     | __ )|  _ \| ____|  / \  / ___| | | |")
		print("| |_| | | | | |   | |     |  _ \| |_) |  _|   / _ \| |   | |_| |")
		print("|  _  | |_| | |___| |___  | |_) |  _ <| |___ / ___ \ |___|  _  |")
		print("|_| |_|\___/|_____|_____| |____/|_| \_\_____/_/   \_\____|_| |_|")


		a = input()
		self.tick()

	def tick(self):


		for row in self.entities:
			for col in row:
				for thingy in col:
					try:
						if thingy.health < 0:
							self.remove_entity(thingy.xPos, thingy.yPos, thingy)
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
			self.say("ur ded rip in peace")
			self.remove_entity(self.player.xPos, self.player.yPos, self.player)

		self.time += 1

		self.render()

		if random.randint(1, 100) == 1:
			self.hull_breach()

def run():
	guy = characters.Knight(None, 1, 1)
	game = Game(guy, 70, 20, 5, 5)
	guy.game = game

	inv = False

	while 1:
		inn = getch.__call__()
		if inn == "up":
			game.player.move(game, 0, -1)
			game.tick()
		elif inn == "down":
			game.player.move(game, 0, 1)
			game.tick()
		elif inn == "left":
			game.player.move(game, -1, 0)
			game.tick()
		elif inn == "right":
			game.player.move(game, 1, 0)
			game.tick()
		elif inn == "q":
			os.system("clear")
			print("bai")
			sys.exit()
		elif inn == "i":
			if not inv:
				game.render_inventory()
				inv = not inv
			else:
				game.tick()
				inv = not inv
		elif inn == ",":
			if game.get_entity_icon(game.player.xPos, game.player.yPos, -2) != "0" and game.get_entity_icon(game.player.xPos, game.player.yPos, -2) != " ":
				game.say("you picked up the " + game.get_entity(game.player.xPos, game.player.yPos, -2).description + " " + game.get_entity(game.player.xPos, game.player.yPos, -2).name)
				game.player.pick_up(game.get_entity(game.player.xPos, game.player.yPos, -2))
			game.tick()
		elif inn == "a":

			#inn = getch.__call__()
			game.render_inventory("What do you want to use or apply?")
			inn = False
			while inn == False:
				inn = getch.__call__()
				game.render_inventory("What do you want to use or apply?")
			if inn == "1":
				game.say("You use 1")
				game.render()
			else:
				game.say("you don't have that, silly")
				game.render()

		elif inn == "t":
			game.render_inventory("What do you want to throw?")
			inn = False
			while inn == False:
				inn = getch.__call__()
				game.render_inventory("What do you want to throw?")
			if inn == "1":
				game.render()
				dum = False
				while dum == False:
					dum = getch.__call__()
					game.say("What direction do you want to throw the " + game.player.inventory.items[0].description + " " + game.player.inventory.items[0].name + "?")
					game.render()
				print(dum + "Aoeu")
				if dum == "down":
					print("HUEHUEHUEHUEH")
					game.set_entity(game.player.xPos, game.player.yPos + game.player.strength * 3 + random.randint(-1, 2), game.player.inventory.items[0])
					game.player.inventory.remove_item(game.player.inventory.items[0])
					game.render()



		elif inn == " ":
			game.tick()
		else:
			pass


run()
