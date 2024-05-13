from math import gcd


class Fraction:
    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            self._numerator, self._denominator = list(map(int, args[0].split("/")))
        elif len(args) == 2:
            self._numerator, self._denominator = args
        self._shorten()

    def _shorten(self):
        gcd_value = gcd(self._numerator, self._denominator)
        if gcd_value != 1:
            self._numerator //= gcd_value
            self._denominator //= gcd_value

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

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
