from collections import defaultdict
# from dataclasses import dataclass


class Number:
    def __init__(self, positions: str):
        self.positions = set(positions)
        self.size = len(positions)

    # @property
    # def size(self) -> int:
    #     return len(self.positions)

    def print(self) -> None:
        display = ""
        nl = "\n"
        display += " aaaa \n" if "a" in self.positions else " .... \n"
        display += f"{['.', 'b']['b' in self.positions]}    {['.', 'c']['c' in self.positions]}{nl}" * 2
        display += " dddd \n" if "d" in self.positions else " .... \n"
        display += f"{['.', 'e']['e' in self.positions]}    {['.', 'f']['f' in self.positions]}{nl}" * 2
        display += " gggg \n" if "g" in self.positions else " .... "
        print(display)


numbers = {
    "zero": Number("abcefg"),
    "one": Number("cf"),
    "two": Number("acdeg"),
    "three": Number("acdfg"),
    "four": Number("bcdf"),
    "five": Number("abdfg"),
    "six": Number("abdefg"),
    "seven": Number("acf"),
    "eight": Number("abcdefg"),
    "nine": Number("abcdfg"),
}

possibilities = defaultdict(list)
for k, v in numbers.items():
    # print(k)
    possibilities[v.size].append((k, v))
    # v.print()
# print(possibilities)
used = defaultdict(set)
# for (s, (k, v)) in possibilities.items():
for (size, pos) in possibilities.items():
    for name, number in pos:
        used[size] |= number.positions

unused = defaultdict(set)
for size, positions in used.items():
    unused[size] = set("abcdefg") - positions

frequencies = defaultdict(int)
for number in numbers.values():
    for position in number.positions:
        frequencies[position] += 1

print("Used:")
print(used)
print("Unused:")
print(unused)
print("Frequencies:")
print(frequencies)

# with open("tests/day8.txt", "r") as file:
with open("inputs/day8.txt", "r") as file:
    total = 0
    for line in file:
        # print(line)
        inputs, outputs = line.split("|")
        for output in outputs.split():
            if len(output.strip()) in (2, 4, 3, 7):
                total += 1
    print(total)
