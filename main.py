import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            if c == "\x1b":
            	c = sys.stdin.read(1)
            	if c == "[":
            		c = sys.stdin.read(1)
            		if c == "A":
            			print("up arrow")
            		elif c == "B":
            			print("down arrow")
            		elif c == "C":
            			print("right arrow")
            		elif c == "D":
            			print("left arrow")

        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def run():
	pass