class Rectangle:

    def __init__(self, first: (float, float), second: (float, float)):
        self.x1 = min(first[0], second[0])
        self.y1 = min(first[1], second[1])
        self.x2 = first[0] + second[0] - self.x1
        self.y2 = first[1] + second[1] - self.y1

    def area(self) -> float:
        return round((self.x2 - self.x1) * (self.y2 - self.y1), 2)

    def perimeter(self) -> float:
        return round((self.x2 - self.x1) * 2 + (self.y2 - self.y1) * 2, 2)
