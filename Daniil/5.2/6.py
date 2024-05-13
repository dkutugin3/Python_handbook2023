from math import gcd


class Fraction:
    def __init__(self, *args) -> None:
        self.sign = 1
        if len(args) == 1 and isinstance(args[0], str):
            self._numerator, self._denominator = list(map(int, args[0].split("/")))
        elif len(args) == 2:
            self._numerator, self._denominator = args
        self._shorten()

    def _shorten(self):
        if self._denominator < 0:
            self.sign *= -1
        if self._numerator < 0:
            self.sign *= -1

        self._numerator = abs(self._numerator)
        self._denominator = abs(self._denominator)

        gcd_value = gcd(abs(self._numerator), self._denominator)
        if gcd_value != 1:
            self._numerator //= gcd_value
            self._denominator //= gcd_value

    def __str__(self):
        return f"{'-' if self.sign == -1 else ''}{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction('{str(self)}')"

    def numerator(self, value=None):
        if not value:
            return self._numerator
        self._numerator = value
        self._shorten()

    def denominator(self, value=None):
        if value:
            self._denominator = value
            self._shorten()
        return self._denominator

    def __neg__(self):
        return Fraction(-self._numerator * self.sign, self._denominator)

    def __add__(self, other):
        return Fraction(
            self._numerator * self.sign * other._denominator
            + other._numerator * other.sign * self._denominator,
            self._denominator * other._denominator,
        )

    def __sub__(self, other):
        return Fraction(
            self._numerator * self.sign * other._denominator
            - other._numerator * other.sign * self._denominator,
            self._denominator * other._denominator,
        )

    def __iadd__(self, other):
        self.__init__(
            self._numerator * self.sign * other._denominator
            + other._numerator * other.sign * self._denominator,
            self._denominator * other._denominator,
        )
        return self

    def __isub__(self, other):
        self.__init__(
            self._numerator * self.sign * other._denominator
            - other._numerator * other.sign * self._denominator,
            self._denominator * other._denominator,
        )
        return self
