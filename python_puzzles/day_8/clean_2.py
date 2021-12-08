from collections import defaultdict

numbers = {
    frozenset("abcefg"): 0,
    frozenset("cf"): 1,
    frozenset("acdeg"): 2,
    frozenset("acdfg"): 3,
    frozenset("bcdf"): 4,
    frozenset("abdfg"): 5,
    frozenset("abdefg"): 6,
    frozenset("acf"): 7,
    frozenset("abcdefg"): 8,
    frozenset("abcdfg"): 9,
}


class Display:
    def __init__(self, numbers: list[str]):
        self.numbers = [set(num.strip()) for num in numbers]
        self.key_map = {}

    def solve(self):
        freq = defaultdict(int)
        used_per_size = defaultdict(set)
        for num in self.numbers:
            for digit in num:
                freq[digit] += 1
            used_per_size[len(num)] |= num
        inv_freq = defaultdict(list)
        for k, v in freq.items():
            inv_freq[v].append(k)
        self.key_map[inv_freq[9][0]] = "f"
        self.key_map[inv_freq[4][0]] = "e"
        self.key_map[inv_freq[6][0]] = "b"
        self.key_map[next(key for key in used_per_size[2] if key not in inv_freq[9])] = "c"
        self.key_map[next(key for key in inv_freq[8] if key not in used_per_size[2])] = "a"
        self.key_map[next(key for key in inv_freq[7] if key in used_per_size[4] and key not in used_per_size[3])] = "d"
        self.key_map[next(key for key in inv_freq[7] if key not in used_per_size[4] and key not in used_per_size[3])] = "g"

    def translate(self, sequence: str):
        return "".join(self.key_map.get(char) for char in sequence)


# with open("tests/day8.txt", "r") as file:
with open("inputs/day8.txt", "r") as file:
    total = 0
    for line in file:
        inputs, outputs = line.split("|")
        display = Display(inputs.split())
        display.solve()
        for i, seq in enumerate(outputs.split()):
            seq = display.translate(seq)
            total += numbers[frozenset(seq)] * (10 ** (3 - i))
    print(total)
