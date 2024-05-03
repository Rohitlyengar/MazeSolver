from graphics import (Window, Point, Line)
from maze import Maze

def main():
    win = Window(800, 600)

    Maze(0, 0, 10, 10, 50, 50, win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
