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
        self.x1 = round(dx + self.x1, 2)
        self.y2 = round(dy + self.y2, 2)
        self.x2 = round(self.x1 + size[0], 2)
        self.y1 = round(self.y2 - size[1], 2)

    def resize(self, width, height):
        self.x2, self.y1 = self.get_pos()
        self.x2 = round(width + self.x2, 2)
        self.y1 = round(self.y1 - height, 2)

    def get_mid(self):
        return (round((self.x2 + self.x1) / 2, 2), round((self.y2 + self.y1) / 2), 2)

    def get_width(self):
        return abs(self.x2 - self.x1)

    def get_height(self):
        return abs(self.y2 - self.y1)

    def turn(self):
        diff = self.get_width() - self.get_height()
        self.resize(round(self.get_height(), 2), round(self.get_width(), 2))
        self.move(round(diff / 2, 2), round(diff / 2, 2))

    def scale(self, factor: float):
        dx = self.get_width() * (factor - 1)
        dy = self.get_height() * (factor - 1)
        self.resize(round(self.get_width() * factor, 2),
                    round(self.get_height() * factor, 2))
        self.move(round(-dx / 2, 2), round(dy / 2, 2))
