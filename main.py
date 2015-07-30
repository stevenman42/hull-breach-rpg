import os, sys
import input
import characters
import info


# the doodad that gets the keyboard input
getch = input._GetchUnix()


# for i in range(10):
#     print(getch.__call__())
    #getch.__call__()



class Game(object):
	def __init__(self, Character, width=10, height=10, playerX=5, playerY=5):

		self.player = Character
		self.map = []
		self.entities = []
		self.info = info.Info(self.player)

		for i in range(height):
			self.map.append([])
			self.entities.append([])
			for j in range(width):
				self.map[i].append(".")
				self.entities[i].append(" ")

		self.height = len(self.map)
		self.width = len(self.map[0])

		self.entities[self.player.yPos][self.player.xPos] = "0"

		self.render()
		
	def render(self):
		os.system("clear")

		self.info.render()

		for i in range(self.height):
			for j in range(self.width):
				if self.entities[i][j] == " ":
					sys.stdout.write(self.map[i][j])
				elif self.entities[i][j] != " ":
					sys.stdout.write(self.map[i][j])
			sys.stdout.write("\n")

	def render_inventory(self):
		os.system("clear")
		for i in self.player.inventory:
			print(i)



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


		else:
			pass



run()
