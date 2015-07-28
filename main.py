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

		self.map[playerY][playerX] = "0"

		
		
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
		if getch.__call__() == "up":
			game.player.move(0, -1)
			game.tick()
		elif getch.__call__() == "down":
			game.player.move(0, 1)
			game.tick()
		elif getch.__call__() == "left":
			game.player.move(-1, 0)
			game.tick()
		elif getch.__call__() == "right":
			game.player.move(0, -1)
			game.tick()
		elif getch.__call__() == "a":
			sys.exit()



run()
