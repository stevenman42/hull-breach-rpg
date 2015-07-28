import os, sys
import input


# the doodad that gets the keyboard input
getch = input._GetchUnix()


# for i in range(10):
#     print(getch.__call__())
    #getch.__call__()



class Game(object):
	def __init__(self, width=10, height=10, playerX=5, playerY=5, Player):

		self.map = []

		for i in range(height):
			self.map.append([])
			for j in range(width):
				self.map[i].append(".")

		self.height = len(self.map)
		self.width = len(self.map[0])

		self.map[playerY][playerX] = "0"

		
		
		for i in range(self.height):
			for j in range(self.width):
				sys.stdout.write(self.map[i][j])
			sys.stdout.write("\n")

	def tick(self):


def run():
	game = Game(20, 20, 5, 5)

run()
