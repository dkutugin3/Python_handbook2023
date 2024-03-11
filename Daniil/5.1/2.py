class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def length(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return round((dx ** 2 + dy ** 2) ** 0.5, 2)
