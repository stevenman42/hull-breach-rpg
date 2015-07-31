import os, sys, random
import input
import characters
import info
import entities
import monsters



# the doodad that gets the keyboard input
getch = input._GetchUnix()


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

				# HAHAH 3D MATRICES WHAT R U GONNA DO ABOUT IT
				self.entities[i].append([])
				self.entity_icons[i].append([])



		self.height = len(self.map)
		self.width = len(self.map[0])


		self.add_entity(0, 0, self.player)

		# TEST CODE PLS IGNORE
		#self.add_entity(5, 5, entities.Book("Super red", 5, 5))
		self.add_entity(4, 4, monsters.Orc(4, 4))


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


	def render_inventory(self):
		os.system("clear")
		print("Inventory")
		print("_" * 20)
		print("|")
		for i in self.player.inventory:
			print("|   " + i + "   |")

	def say(self, dialogue):
		self.info.add_dialogue(dialogue)




	def tick(self):

		for row in self.entities:
			for col in row:
				for thingy in col:
					try:
						if thingy.health < 0:
							self.remove_entity(thingy.xPos, thingy.yPos, thingy)
							if thingy == self.player:
								self.say("Ur ded rip in peace")
							kill_adj = ["brutally", "efficiently", "swiftly", "messily", "violently", "cheerfully"][random.randint(0,5)]
							kill_msg = ["murder", "slaughter", "destroy", "annihilate", "obliterate", "kill", "massacre"][random.randint(0,6)]
							self.say("You " + kill_adj + " " + kill_msg + " the " + thingy.name)
					except AttributeError:
						# this occurs when the entity doesn't have any health, like a book or other item
						pass
					#thingy.tick(self)

		for entity in self.entity_array:
			entity.tick(self)

		self.time += 1

		self.render()
def run():
	guy = characters.Knight(None)
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
		elif inn == " ":
			game.tick()
		else:
			game.tick()


run()
