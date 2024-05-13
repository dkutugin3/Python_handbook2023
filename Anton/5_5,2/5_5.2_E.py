from math import gcd


class Fraction:

    def __init__(self, x: int | str, y: int = 1):
        if isinstance(x, str):
            try:
                (x, y) = tuple(map(int, x.split('/')))
            except ValueError:
                x = int(x)

        self.num = x
        self.den = y
        self.sign = 1

        self._reduce()

    def __neg__(self):
        new_fract = Fraction(-(self.sign * self.num), self.den)
        return new_fract

    def numerator(self, number: int = None) -> int | None:
        if not number:
            return self.num
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
        return f"{self.sign * self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction('{self.sign * self.num}/{self.den}')"

    def _reduce(self):
        self.num *= self.sign
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

        g = gcd(abs(self.num), abs(self.den))
        self.num //= g
        self.den //= g

        self.sign = abs(self.num) // self.num
        self.num = abs(self.num)
