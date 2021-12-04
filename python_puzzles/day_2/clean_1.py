class Submarine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def forward(self, dx):
        self.x += dx

    def down(self, dy):
        self.y += dy

    def up(self, dy):
        self.y -= dy

    def __repr__(self):
        return f"Submarine({self.x}, {self.y})"


sub = Submarine(0, 0)

ops = {
    "forward": sub.forward,
    "down": sub.down,
    "up": sub.up,
}

with open("inputs/day2.txt", "r") as file:
    for line in file:
        op, val = line.split()
        ops.get(op)(int(val))

print(sub)
print(sub.x * sub.y)
