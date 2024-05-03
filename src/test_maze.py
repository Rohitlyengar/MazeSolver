import unittest
from maze import Maze
from graphics import Window

class MazeTest(unittest.TestCase):
    def test_maze_1(self):
        num_of_rows = 10
        num_of_cols = 12

        win = Window(800, 600)
        m1 = Maze(100, 75, num_of_rows, num_of_cols, 50, 50, win)

        self.assertEqual(num_of_cols, len(m1._cells))
        self.assertEqual(num_of_rows, len(m1._cells[0]))

    def test_maze_2(self):
        num_of_rows = 50
        num_of_cols = 50

        win = Window(800, 600)
        m1 = Maze(100, 75, num_of_rows, num_of_cols, 25, 25, win)

        self.assertEqual(num_of_cols, len(m1._cells))
        self.assertEqual(num_of_rows, len(m1._cells[0]))

    def test_maze_3(self):
        num_of_rows = 25
        num_of_cols = 25

        win = Window(800, 600)
        m1 = Maze(100, 75, num_of_rows, num_of_cols, 25, 25, win)

        self.assertEqual(num_of_cols, len(m1._cells))
        self.assertEqual(num_of_rows, len(m1._cells[0]))

if __name__ == "__main__":
    unittest.main()