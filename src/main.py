from graphics import (Window, Point, Line)
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win)

    cell1.has_top_wall = False
    cell1.draw(50, 50, 100, 100)

    win.wait_for_close()

if __name__ == '__main__':
    main()
