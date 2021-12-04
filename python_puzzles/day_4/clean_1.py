# from itertools import product
from dataclasses import dataclass


@dataclass
class Cell:
    value: int
    finished: bool = False

    def __repr__(self):
        return f"{self.value:02}{'T' if self.finished else 'F'}"


class Bingo:
    def __init__(self, data: list[list[Cell]]):
        self.data = data
        self.numbers = set(n.value for row in data for n in row)

    def add_number(self, number: int):
        if number in self.numbers:
            for row in self.data:
                for cell in row:
                    if cell.value == number:
                        cell.finished = True
                        return True
        return False

    def is_win(self):
        return any(all(cell.finished for cell in row) for row in self.data) or any(all(cell.finished for cell in col) for col in list(zip(*self.data)))

    def __repr__(self):
        nl = '\n'
        return f"Board({nl.join(repr(row) for row in self.data)})"

    def score(self):
        return sum(sum(cell.value for cell in row if not cell.finished) for row in self.data)


# self = Bingo([[Cell(1), Cell(2)], [Cell(3), Cell(4)]])
# list(zip(*[[1, 2], [3, 4]]))

# self.numbers
# file = open("tests/day4.txt")

# with open("tests/day4.txt", "r") as file:
with open("inputs/day4.txt", "r") as file:
    draws = [int(num) for num in file.readline().split(",")]
    file.readline()
    boards = []
    board = []
    for line in file:
        # print(line)
        if line == "\n":
            boards.append(Bingo(board))
            board = []
        else:
            board.append([Cell(int(num)) for num in line.split()])
    boards.append(Bingo(board))  # The End of File line break does not counts as a line break I guess?

    winners = []
    for number in draws:
        for board in boards:
            # board.add_number returns True if it changed it's state
            if board.add_number(number) and board.is_win():
                winners.append(board)
            # print(board)

        if winners:
            # print(winners)
            print(*boards, sep = "\n\n")
            break
    else:
        print("No winners?")
    print("Finished!")
    print("Number of winners:", len(winners))
    print("Score of the winner:", sc := winners.pop().score())
    print("...multiplied by the last number:", sc * number)
# file.close()
