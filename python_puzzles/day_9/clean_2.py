class Board:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def check_lowest(self):
        # return [cell for y, row in enumerate(self.board) for x, cell in enumerate(row) if cell < min(self.get_nearby(x, y))]
        return [(cell, x, y) for y, row in enumerate(self.board) for x, cell in enumerate(row) if cell < min(self.get_nearby(x, y))]
        # return [cell for y, row in enumerate(self.board) for x, cell in enumerate(row) if cell <= min(self.get_nearby(x, y))]

    def get_nearby(self, x, y):
        n = []
        for offx, offy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x+offx) < 0 or (y+offy) < 0 or (x+offx) >= self.width or (y+offy) >= self.height:
                continue
            n.append(self.board[y + offy][x + offx])
            # n.append((y + offy, x + offx))
        return n

    def get_basin(self, current, _x, _y, visited):
        # if visited is None:
        #     visited = set()
        for offx, offy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = _x+offx
            y = _y+offy
            if x < 0 or y < 0 or x >= self.width or y >= self.height:
                continue
            cell = self.board[y][x]
            if current < cell < 9 and (cell, x, y) not in visited:
                visited.add((cell, x, y))
                self.get_basin(cell, x, y, visited)
        return visited


# with open("tests/day9.txt", "r") as file:
with open("inputs/day9.txt", "r") as file:
    board = Board([[int(num) for num in list(row.strip())] for row in file])
    lowest = board.check_lowest()
    # print(lowest)
    basins = [board.get_basin(*low, {low}) for low in lowest]
    basins = [len(basin) for basin in basins]
    basins.sort(reverse=True)
    # print(basins)
    print(basins[0] * basins[1] * basins[2])
    # print("Result: ", sum(1 + n for n in lowest))
