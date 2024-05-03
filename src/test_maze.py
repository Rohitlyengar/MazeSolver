import unittest
from maze import Maze
from graphics import Window

class MazeTest(unittest.TestCase):
    def test_maze(self):
        num_of_rows = 10
        num_of_cols = 12

        win = Window(800, 600)
        m1 = Maze(0, 0, num_of_rows, num_of_cols, 50, 50, win)

        self.assertEqual(num_of_cols, len(m1._cells))
        self.assertEqual(num_of_rows, len(m1._cells[0]))

if __name__ == "__main__":
    unittest.main()