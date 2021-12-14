from collections import Counter, defaultdict
from math import ceil

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


pair_counts = defaultdict(int)
for pair in get_pairs(template):
    pair_counts[pair] += 1

# print(pair_counts)

for _ in range(40):
    new_pairs = defaultdict(int)
    for ((left, right), count) in pair_counts.items():
        middle = pairs.get((left, right))
        new_pairs[(left, middle)] += count
        new_pairs[(middle, right)] += count
    pair_counts = new_pairs
    # print(pair_counts)


letter_counts = defaultdict(int)
for (left, right), value in pair_counts.items():
    letter_counts[left] += value
    letter_counts[right] += value

# might not work if the very first and the very last letters are the same. whatever.
letter_counts = {k: ceil(v/2) for k, v in letter_counts.items()}

print(letter_counts)
print(max(letter_counts.values()) - min(letter_counts.values()))
# counts = Counter(template)
# print(len(template))
# print(counts)
# print(max(counts.values()) - min(counts.values()))
