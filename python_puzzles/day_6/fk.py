from collections import defaultdict

with open("tests/day6.txt", "r") as file:
    fishes = defaultdict(int)
    for fish in file.readline().strip().split(","):
        fishes[fish] += 1
    print(fishes)


with open("inputs/day6.txt", "r") as file:
    fishes = defaultdict(int)
    for fish in file.readline().strip().split(","):
        fishes[fish] += 1
    print(fishes)
