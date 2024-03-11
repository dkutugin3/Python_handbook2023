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
