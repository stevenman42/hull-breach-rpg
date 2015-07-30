import os, sys
import input
import characters
import info
import entities


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

		for i in range(height):
			self.map.append([])
			self.entities.append([])
			self.entity_icons.append([])
			for j in range(width):
				self.map[i].append(".")

				# HAHAH 3D MATRICES WHAT R U GONNA DO ABOUT IT
				self.entities[i].append([])
				self.entity_icons[i].append([])

		for i in self.entities:
			print(i)

		self.height = len(self.map)
		self.width = len(self.map[0])


		self.add_entity(0, 0, self.player)

		# TEST CODE PLS IGNORE
		self.add_entity(5, 5, entities.Book("red"))


		self.render()

	def add_entity(self, xPos, yPos, entity):
		self.entities[yPos][xPos].append(entity)
		self.entity_icons[yPos][xPos].append(entity.icon)
		
	def render(self):
		os.system("clear")

		print(self.entity_icons[0])

		self.info.render()

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

			sys.stdout.write("\n")

	def render_inventory(self):
		os.system("clear")
		print("Inventory")
		print("_" * 20)
		print("|")
		for i in self.player.inventory:
			print("|   " + i + "   |")



	def tick(self):
		self.render()

def run():
	game = Game(characters.Knight(), 20, 20, 5, 5)

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
			if game.entities[game.player.yPos][game.player.xPos] != " ":
				print("you picked it up")


		else:
			pass



run()
