from graphics import (Window, Point, Line)
from maze import Maze

def main():

    rows = int(input("Enter the Number of Rows: "))
    cols = int(input("Enter the Number of Columns: "))

    win = Window(800, 600)
    maze = Maze(50, 50, rows, cols, 50, 50, win)

    if maze.solve():
        print("Maze solved!")
    else:
        print("Maze can not be solved!")

    win.wait_for_close()

if __name__ == '__main__':
    main()
