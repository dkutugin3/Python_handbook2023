from math import gcd


class Fraction:

    def __init__(self, x: int | str, y: int = None):
        if not y:
            (x, y) = tuple(map(int, x.split('/')))

        self.num = x
        self.den = y

        self._reduce()

    def numerator(self, number: int = None) -> int | None:
        if not number:
            return abs(self.num)
        else:
            self.num = number
            self._reduce()

    def denominator(self, number: int = None) -> int | None:
        if not number:
            return self.den
        else:
            self.den = number
            self._reduce()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def _reduce(self):
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

        g = gcd(abs(self.num), self.den)
        self.num //= g
        self.den //= g
