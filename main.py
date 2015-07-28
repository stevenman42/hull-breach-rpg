import os, sys
import input
import characters


# the doodad that gets the keyboard input
getch = input._GetchUnix()


# for i in range(10):
#     print(getch.__call__())
    #getch.__call__()



class Game(object):
	def __init__(self, Character, width=10, height=10, playerX=5, playerY=5):

		self.player = Character
		self.map = []

		for i in range(height):
			self.map.append([])
			for j in range(width):
				self.map[i].append(".")

		self.height = len(self.map)
		self.width = len(self.map[0])

		self.map[self.player.yPos][self.player.xPos] = "0"

		self.render()
		
	def render(self):
		os.system("clear")
		for i in range(self.height):
			for j in range(self.width):
				sys.stdout.write(self.map[i][j])
			sys.stdout.write("\n")

	def tick(self):
		self.render()

def run():
	game = Game(characters.Knight(), 20, 20, 5, 5)

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
			print("bai")
			sys.exit()
		else:
			pass



run()
