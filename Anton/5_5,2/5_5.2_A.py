class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def move(self, x: int | float, y: int | float):
        self.x += x
        self.y += y

    def length(self, point) -> float:
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *pos):
        match len(pos):
            case 0:
                super().__init__(0, 0)
            case 1:
                pos = pos[0]
                super().__init__(pos[0], pos[1])
            case 2:
                super().__init__(*pos)
