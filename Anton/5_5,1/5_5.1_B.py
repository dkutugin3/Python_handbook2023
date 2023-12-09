class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def move(self, x: int | float, y: int | float):
        self.x += x
        self.y += y

    def length(self, point) -> float:
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)
