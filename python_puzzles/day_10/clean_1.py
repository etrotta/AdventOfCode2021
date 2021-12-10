CHARMAP = {
    "<": ">",
    "{": "}",
    "[": "]",
    "(": ")",
}


def findInvalid(line):
    path = []
    for char in line:
        if char in CHARMAP.keys():
            path.append(CHARMAP.get(char))
        elif char in CHARMAP.values():
            if char == path.pop():
                continue
            else:
                return char


scores = {
    None: 0,
    ">": 25137,
    "}": 1197,
    "]": 57,
    ")": 3,
}
# with open("tests/day10.txt", "r") as file:
with open("inputs/day10.txt", "r") as file:
    total = 0
    for line in file:
        print(findInvalid(line))
        print(scores.get(findInvalid(line)))
        total += scores.get(findInvalid(line))
    print(total)
