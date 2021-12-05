from math import copysign
# from collections import defaultdict


class Table:
    def __init__(self, width, height):
        self.data = [[0 for _ in range(width)] for _ in range(height)]

    def __repr__(self):
        return f"Table({self.width, self.height})"

    def add(self, x, y):
        self.data[y][x] += 1

    def print(self):
        res = ""
        for row in self.data:
            for cell in row:
                if cell == 0:
                    res += "."
                else:
                    res += str(cell)
            res += "\n"
        print(res)

    def score(self):
        return sum(sum(1 for cell in col if cell >= 2) for col in self.data)


# table = defaultdict(int)
table = Table(1000, 1000)
# table = Table(10, 10)
# with open("tests/day5.txt", "r") as file:
with open("inputs/day5.txt", "r") as file:
    for line in file:
        start, end = line.replace(" ", "").split("->")
        start, end = tuple(int(pos) for pos in start.split(",")), tuple(int(pos) for pos in end.split(","))
        if start[0] == end[0]:  # or start[1] == end[1]:
            x = start[0]
            sign = int(copysign(1, (end[1])-start[1]))
            for y in range(start[1], end[1] + sign, sign):
                # table[(x, y)] += 1
                table.add(x, y)
        elif start[1] == end[1]:
            y = start[1]
            sign = int(copysign(1, (end[0])-start[0]))
            for x in range(start[0], end[0] + sign, sign):
                # table[(x, y)] += 1
                table.add(x, y)
        else:
            sign_x = int(copysign(1, (end[0])-start[0]))
            sign_y = int(copysign(1, (end[1])-start[1]))
            for x, y in zip(range(start[0], end[0] + sign_x, sign_x), range(start[1], end[1] + sign_y, sign_y)):
                table.add(x, y)
    # print(table)
    # table.print()
    print(table.score())
