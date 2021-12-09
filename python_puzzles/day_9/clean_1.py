class Board:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def check_lowest(self):
        return [cell for y, row in enumerate(self.board) for x, cell in enumerate(row) if cell < min(self.get_nearby(x, y))]
        # return [cell for y, row in enumerate(self.board) for x, cell in enumerate(row) if cell <= min(self.get_nearby(x, y))]

    def get_nearby(self, x, y):
        n = []
        for offx, offy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x+offx) < 0 or (y+offy) < 0 or (x+offx) >= self.width or (y+offy) >= self.height:
                continue
            # try:
            print(x, y, offx, offy)
            n.append(self.board[y + offy][x + offx])
            # except IndexError:
            #    # continue
        return n


# with open("tests/day9.txt", "r") as file:
with open("inputs/day9.txt", "r") as file:
    board = Board([[int(num) for num in list(row.strip())] for row in file])
    lowest = board.check_lowest()
    print(lowest)
    print("Result: ", sum(1 + n for n in lowest))
