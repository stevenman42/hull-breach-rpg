import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)


def get_input():
	try:
		while 1:
			try:
				c = sys.stdin.read(1)
				if c == "\x1b":
					c = sys.stdin.read(1)
					if c == "[":
						c = sys.stdin.read(1)
						if c == "A":
							return("up arrow")
						elif c == "B":
							return("down arrow")
						elif c == "C":
							return("right arrow")
						elif c == "D":
							return("left arrow")

			except IOError: pass

	finally:
		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def run():
	while 1:
		print(get_input())
		print("hue")

run()