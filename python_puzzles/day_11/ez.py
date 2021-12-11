def get_surroundings(x, y):
    return [
        (x + 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]


class Cell:
    def __init__(self, energy: int):
        self.energy = energy
        self.flashed = False

    def tick(self) -> bool:
        if self.flashed:
            return False
        if self.energy >= 9:
            self.flashed = True
            self.energy = 0
            return True
        else:
            self.energy += 1
        return False

    def add(self) -> None:
        if not self.flashed:
            self.energy += 1

    def check(self) -> bool:
        if self.flashed:
            return False
        if self.energy >= 9:
            self.flashed = True
            self.energy = 0
            return True
        return False

    def reset(self):
        _old = self.flashed
        self.flashed = False
        return not _old


class Board:
    def __init__(self, values: list[list[int]]):
        self.grid = [[Cell(value) for value in row] for row in values]
        self.total_ticks = 0

    def step(self):
        to_check = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell.tick():
                    to_check.extend(get_surroundings(x, y))
                    self.total_ticks += 1

        for x, y in to_check:
            if 0 <= x < 10 and 0 <= y < 10:
                if self.grid[y][x].tick():
                    to_check.extend(get_surroundings(x, y))
                    self.total_ticks += 1

        _all = True
        for row in self.grid:
            for cell in row:
                if cell.reset():
                    _all = False
        if _all:
            return True
        return False

    def display(self):
        return "\n".join("".join(str(cell.energy) for cell in row) for row in self.grid)


# with open("tests/day11.txt", "r") as file:
with open("inputs/day11.txt", "r") as file:
    values = [[int(val) for val in line.strip()] for line in file]
    board = Board(values)
    # print(board.display())
    for s in range(1, 1000):
        # print()
        if board.step():
            print("Sync!", s)
            break
        # print(board.display())
    # print()
    # print("Result: ", board.total_ticks)
