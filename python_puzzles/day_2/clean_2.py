class Submarine:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self.aim = aim

    def forward(self, dx):
        self.x += dx
        self.y += dx * self.aim

    def down(self, dy):
        self.aim += dy

    def up(self, dy):
        self.aim -= dy

    def __repr__(self):
        return f"Submarine({self.x}, {self.y}, {self.aim})"


sub = Submarine(0, 0, 0)

ops = {
    "forward": sub.forward,
    "down": sub.down,
    "up": sub.up,
}

with open("inputs/day2.txt", "r") as file:
    # with open("tests/day2.txt", "r") as file:
    for line in file:
        op, val = line.split()
        ops.get(op)(int(val))
        # print(sub)

print(sub)
print(sub.x * sub.y)
