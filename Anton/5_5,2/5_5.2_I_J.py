from math import gcd


class Fraction:
    def __init__(self, x: int | str, y: int = 1):
        if isinstance(x, str):
            try:
                (x, y) = tuple(map(int, x.split('/')))
            except ValueError:
                x = int(x)

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
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __radd__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __iadd__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        self.numerator(self.numerator() * other.denominator() + other.numerator() * self.denominator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __sub__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.denominator() - other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __rsub__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(-self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                             self.denominator() * other.denominator())
        return new_fract

    def __isub__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        self.numerator(self.numerator() * other.denominator() - other.numerator() * self.denominator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __mul__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.numerator(), self.denominator() * other.denominator())
        return new_fract

    def __rmul__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.numerator(), self.denominator() * other.denominator())
        return new_fract

    def __imul__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        self.numerator(self.numerator() * other.numerator())
        self.denominator(self.denominator() * other.denominator())
        return self

    def __truediv__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.numerator() * other.denominator(), self.denominator() * other.numerator())
        return new_fract

    def __rtruediv__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        new_fract = Fraction(self.denominator() * other.numerator(), self.numerator() * other.denominator())
        return new_fract

    def __itruediv__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        self.numerator(self.numerator() * other.denominator())
        self.denominator(self.denominator() * other.numerator())
        return self

    def __str__(self) -> str:
        return f"{self.numerator()}/{self.denominator()}"

    def __repr__(self) -> str:
        return f"Fraction('{self.numerator()}/{self.denominator()}')"

    def __eq__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return self.numerator() == other.numerator() and self.denominator() == other.denominator()

    def __ne__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return not (self == other)

    def __gt__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return self.numerator() * other.denominator() > self.denominator() * other.numerator()

    def __lt__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return self.numerator() * other.denominator() < self.denominator() * other.numerator()

    def __ge__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return not (self < other)

    def __le__(self, other):
        if not (isinstance(other, Fraction)):
            other = Fraction(other)
        return not (self > other)

    def _reduce(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num

        g = gcd(abs(self._num), self._den)
        self._num //= g
        self._den //= g
