# -*- coding: utf-8 -*-

import string

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)

            if ch not in string.lowercase + "1234567890,._=[] ":
                dis = sys.stdin.read(2)
                if(dis == "[A"):
                    #print("up")
                    ch = "up"
                    return ch
                elif (dis == "[B"):
                    #print("down")
                    ch = "down"
                    return ch
                elif (dis == "[C"):
                    #print("right")
                    ch = "right"
                    return ch
                elif (dis == "[D"):
                    #print("left")
                    ch = "left"
                    return ch
            else:
                return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


# getch = _GetchUnix()
# for i in range(10):
#     print(getch.__call__())