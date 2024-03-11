class RedButton:
    def __init__(self) -> None:
        self._count = 0

    def click(self):
        print("Тревога!")
        self._count += 1

    def count(self):
        return self._count
