import re

# dS = v0*t + a*(t**2)/2


def test(dx, dy, min_x, max_x, min_y, max_y):
    x, y = 0, 0
    highest = 0
    while (x <= max_x and y >= min_y):
        if x >= min_x and y <= max_y:
            # return True
            return highest
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        highest = max(highest, y)
        print(x, y)
    return False


def get_valid_x_steps(min_x, max_x):
    valid = {}
    for _dx in range(max_x):
        steps = 0
        dx = _dx
        x = 0
        while (x <= max_x and dx >= 0):
            if x >= min_x:
                valid[_dx] = steps
                break
            steps += 1
            x += dx
            dx -= 1
    return valid


assert test(7, 2, 20, 30, -10, -5), "Failed a test case"

# get_valid_x_steps(20, 30)
# test(7, 2, 20, 30, -10, -5)

# with open("tests/day17.txt", "r") as file:
with open("inputs/day17.txt", "r") as file:
    content = file.read()
    min_x, max_x, min_y, max_y = [int(x) for x in (re.findall(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)\n?", content)[0])]
    S = get_valid_x_steps(min_x, max_x)

# test(41, max_y+1, min_x, max_x, min_y, max_y)
# test(82, max_y+1, min_x, max_x, min_y, max_y)
max(S.items(), key = lambda t: t[1])
# When it reaches y=0, it will be back at the initial Y velocity, but going on the opposite direction.
test(15, -min_y-2, min_x, max_x, min_y, max_y)
test(15, -min_y-1, min_x, max_x, min_y, max_y)
test(15, -min_y, min_x, max_x, min_y, max_y)

print(min_x, max_x, min_y, max_y)
