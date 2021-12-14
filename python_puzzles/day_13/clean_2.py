from collections import namedtuple


def visualise(points):
    map = {}
    max_x = 0
    max_y = 0
    for x, y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        map[(x, y)] = True

    result = []
    for y in range(max_y + 1):
        line = []
        # for x in range(1 + int(max_x * 1.25)):
        for x in range(max_x + 1):
            # line.append("#" if map.get((x, y)) else ".")
            line.append(u"\u25A0" if map.get((x, y)) else " ")
        result.append(line)

    # for x in range(max_x + 1):
    #     if all(row[x] == "." for row in result):
    #         for row in result:
    #             row[x] = "   "
    return "\n".join("".join(row) for row in result)


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

# if True:
#    # axis, position = next(iter(folds))
for axis, position in folds:
    for i, point in enumerate(points):
        if axis == "x":
            if point.x > position:
                points[i] = Point(2 * position - point.x, point.y)
        else:
            if point.y > position:
                points[i] = Point(point.x, 2 * position - point.y)

print(visualise(points))

# print(points)
# print(len(set(points)))
