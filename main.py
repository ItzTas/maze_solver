from graphics import *
from cell import Cell

def main():
    win = Window(800, 880)
    c = Cell(win)
    c.draw(300, 900, 10, 400)
    win.wait_for_close()

main()