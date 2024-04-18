from graphics import *
from cell import Cell
from maze import Maze

def main():
    num_rows = 18
    num_cols = 16
    margin1 = 10
    margin2 = 10
    screen_x = 890
    screen_y = 690
    cell_size_x = (screen_x - 2 * margin1) / num_cols
    cell_size_y = (screen_y - 2 * margin2) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin1, margin2, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()


main()