class Cell:

    def __init__(self, state: str):
        self.state = state

    def change_state(self, new_state: str):
        self.state = new_state

    def status(self) -> str:
        return self.state


class Checkers:

    def __init__(self):
        self.board = [[Cell("W") if (col + row) % 2 == 0 else Cell("X") for col in range(8)] for row in range(3)]
        self.board += [[Cell("X") for col in range(8)] for row in range(2)]
        self.board += [[Cell("B") if (col + row) % 2 == 1 else Cell("X") for col in range(8)] for row in range(3)]

    def move(self, pos1: str, pos2: str):
        row1 = int(pos1[1]) - 1
        col1 = ord(pos1[0]) - ord("A")
        row2 = int(pos2[1]) - 1
        col2 = ord(pos2[0]) - ord("A")

        self.board[row2][col2].change_state(self.board[row1][col1].status())
        self.board[row1][col1].change_state("X")

    def get_cell(self, pos) -> Cell:
        row = int(pos[1]) - 1
        col = ord(pos[0]) - ord("A")
        return self.board[row][col]
