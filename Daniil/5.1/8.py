class Cell:
    def __init__(self, liter, number) -> None:
        if (ord(liter) + ord(number)) % 2 == 0:
            if number <= "3":
                self._status = "W"
            elif number >= "6":
                self._status = "B"
            else:
                self._status = "X"
        else:
            self._status = "X"

    def chg_status(self, new):
        self._status = new

    def status(self):
        return self._status


class Checkers:
    def __init__(self) -> None:
        self.fields = {liter: {number: Cell(liter, number) for number in "12345678"}
                       for liter in "ABCDEFGH"}

    def move(self, f, t):
        self.fields[t[0]][t[1]].chg_status(self.fields[f[0]][f[1]].status())
        self.fields[f[0]][f[1]].chg_status("X")

    def get_cell(self, p):
        return self.fields[p[0]][p[1]]
