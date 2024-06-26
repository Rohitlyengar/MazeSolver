from graphics import (Line, Point)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def get_midpoint(self):
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self._y2) / 2
        return mid_x, mid_y

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


        if self.has_left_wall:
            left_wall_color = "black"
        else:
            left_wall_color = "white"

        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, left_wall_color)


        if self.has_top_wall:
            top_wall_color = "black"
        else:
            top_wall_color = "white"

        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, top_wall_color)


        if self.has_right_wall:
            right_wall_color = "black"
        else:
            right_wall_color = "white"

        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, right_wall_color)

        if self.has_bottom_wall:
            bottom_wall_color = "black"
        else:
            bottom_wall_color = "white"

        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, bottom_wall_color)


    def draw_move(self, to_cell, undo=False):
        p1 = Point(self.get_midpoint()[0], self.get_midpoint()[1])
        p2 = Point(to_cell.get_midpoint()[0], to_cell.get_midpoint()[1])
        line = Line(p1, p2)

        if undo:
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")
