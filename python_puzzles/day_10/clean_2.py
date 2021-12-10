CHARMAP = {
    "<": ">",
    "{": "}",
    "[": "]",
    "(": ")",
}


def findIncomplete(line):
    path = []
    for char in line:
        if char in CHARMAP.keys():
            path.append(CHARMAP.get(char))
        elif char in CHARMAP.values():
            if char != path.pop():
                return []
    return path


score_map = {
    None: 0,
    ">": 4,
    "}": 3,
    "]": 2,
    ")": 1,
}

# with open("tests/day10.txt", "r") as file:
with open("inputs/day10.txt", "r") as file:
    scores = []
    for line in file:
        score = 0
        remainder = findIncomplete(line)
        while remainder:
            score *= 5
            score += score_map.get(remainder.pop())
        if score > 0:
            scores.append(score)

scores.sort()
print(scores[len(scores)//2])
