class Rectangle:

    def __init__(self, first: (float, float), second: (float, float)):
        self.x1 = first[0]
        self.y1 = first[1]
        self.x2 = second[0]
        self.y2 = second[1]

        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1

    def area(self) -> float:
        return round(self.width * self.height, 2)

    def perimeter(self) -> float:
        return round((self.width + self.height) * 2, 2)

    def get_pos(self) -> (float, float):
        return tuple([round(self.x1, 2), round(self.y2, 2)])

    def get_size(self) -> (float, float):
        return tuple([round(self.width, 2), round(self.height, 2)])

    def move(self, dx: float, dy: float):

        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, width: float, height: float):

        self.x2 += width - self.width
        self.y1 -= height - self.height
        self.width = width
        self.height = height
