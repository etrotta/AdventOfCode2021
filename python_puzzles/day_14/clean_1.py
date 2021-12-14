from collections import Counter

pairs = {}


def get_pairs(origin: str):
    for a, b in zip(origin, origin[1:]):
        yield (a, b)


# with open("tests/day14.txt", "r") as file:
with open("inputs/day14.txt", "r") as file:
    template = next(file).strip()
    next(file)
    for line in file:
        inp, out = line.split(" -> ")
        pairs[tuple(inp)] = out.strip()


for _ in range(10):
    new_template = ""
    for left, right in get_pairs(template):
        new_template += left + pairs.get((left, right), "")
    new_template += right
    template = new_template
    # print(new_template)

counts = Counter(template)
print(len(template))
print(counts)
print(max(counts.values()) - min(counts.values()))
