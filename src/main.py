from graphics import (Window, Point, Line)
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell2 = Cell(win)

    cell1.draw(50, 50, 100, 100)
    cell2.draw(125, 125, 200, 200)

    cell1.draw_move(cell2, True)

    win.wait_for_close()

if __name__ == '__main__':
    main()
