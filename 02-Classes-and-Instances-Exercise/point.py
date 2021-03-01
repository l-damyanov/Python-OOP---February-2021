from math import hypot

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x
        return self.x

    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def distance(self, c_x, c_y):
        return hypot(c_x - self.x, c_y - self.y)
