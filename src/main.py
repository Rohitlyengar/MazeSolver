from graphics import (Window, Point, Line)
from maze import Maze

def main():
    win = Window(800, 600)

    m1 = Maze(50, 50, 10, 10, 50, 50, win)

    m1._break_walls_r(0, 0)

    win.wait_for_close()

if __name__ == '__main__':
    main()
