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
        return round((dx**2 + dy**2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(*args)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other: tuple):
        ans = PatchedPoint(self.x, self.y)
        ans.move(other[0], other[1])
        return ans

    def __iadd__(self, other: tuple):
        self.move(other[0], other[1])
        return self
