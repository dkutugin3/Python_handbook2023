from numpy import size


class Rectangle:
    def __init__(self, dot1: tuple, dot2: tuple) -> None:
        x1, y1 = dot1
        x2, y2 = dot2
        self.x1, self.x2 = sorted([x1, x2])
        self.y1, self.y2 = sorted([y1, y2])

    def perimeter(self):
        return round(((self.x2 - self.x1) + (self.y2 - self.y1)) * 2, 2)

    def area(self):
        return round((self.x2 - self.x1) * (self.y2 - self.y1), 2)

    def get_pos(self):
        return round(self.x1, 2), round(self.y2, 2)

    def get_size(self):
        return round(self.x2 - self.x1, 2), round(self.y2 - self.y1, 2)

    def move(self, dx, dy):
        size = self.get_size()
        self.x1 += dx
        self.y2 += dy
        self.x2 = self.x1 + size[0]
        self.y1 = self.y2 - size[1]

    def resize(self, width, height):
        self.x2, self.y1 = self.get_pos()
        self.x2 += width
        self.y1 -= height
