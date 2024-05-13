from math import gcd


class Fraction:
    def __init__(self, x: int | str, y: int = None):
        if not y:
            (x, y) = tuple(map(int, x.split('/')))

        self._num = x
        self._den = y

        self._reduce()

    def numerator(self, number: int = None) -> int | None:
        if not number:
            return self._num
        else:
            self._num = number
            self._reduce()

    def denominator(self, number: int = None) -> int | None:
        if not number:
            return self._den
        else:
            self._den = number
            self._reduce()

    def reverse(self):
        new_fract = Fraction(self.denominator(), self.numerator())
        return new_fract

    def __neg__(self):
        new_fract = Fraction(-self.numerator(), self.denominator())
        return new_fract

    def __add__(self, other):
        new_fract = Fraction(self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __radd__(self, other):
        new_fract = Fraction(self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __iadd__(self, other):
        self.numerator(self.numerator() * other.denominator() + other.numerator() * self.denominator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __sub__(self, other):
        new_fract = Fraction(self.numerator() * other.denominator() - other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __rsub__(self, other):
        new_fract = Fraction(-self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __isub__(self, other):
        self.numerator(self.numerator() * other.denominator() - other.numerator() * self.denominator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __mul__(self, other):
        new_fract = Fraction(self.numerator() * other.numerator(), self.denominator() * other.denominator())
        return new_fract

    def __rmul__(self, other):
        new_fract = Fraction(self.numerator() * other.numerator(), self.denominator() * other.denominator())
        return new_fract

    def __imul__(self, other):
        self.numerator(self.numerator() * other.numerator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __truediv__(self, other):
        new_fract = Fraction(self.numerator() * other.denominator(), self.denominator() * other.numerator())
        return new_fract

    def __rtruediv__(self, other):
        new_fract = Fraction(self.denominator() * other.numerator(), self.numerator() * other.denominator())
        return new_fract

    def __itruediv__(self, other):
        self.numerator(self.numerator() * other.denominator())
        self.denominator(self.denominator() * other.numerator())
        return self

    def __str__(self) -> str:
        return f"{self.numerator()}/{self.denominator()}"

    def __repr__(self) -> str:
        return f"Fraction('{self.numerator()}/{self.denominator()}')"

    def _reduce(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num

        g = gcd(abs(self._num), self._den)
        self._num //= g
        self._den //= g
