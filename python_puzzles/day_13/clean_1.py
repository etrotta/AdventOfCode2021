from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])

# with open("tests/day13.txt", "r") as file:
with open("inputs/day13.txt", "r") as file:
    points = []
    folds = []
    for line in file:
        if line == "\n":
            continue
        try:
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            points.append(Point(x, y))
        except ValueError:
            axis, position = line.split("=")
            axis = axis[-1]
            position = int(position)
            folds.append((axis, position))

# Fold at 10
# Point at 16
# Distance = 6
# Fold - Distance = 4

# for axis, position in folds:
if True:
    axis, position = next(iter(folds))
    for i, point in enumerate(points):
        if axis == "x":
            if point.x > position:
                points[i] = Point(2 * position - point.x, point.y)
        else:
            if point.y > position:
                points[i] = Point(point.x, 2 * position - point.y)

# print(points)
print(len(set(points)))
