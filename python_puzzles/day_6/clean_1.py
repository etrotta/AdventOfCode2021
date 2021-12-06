total_after_80_days = {}
for starting in range(1, 7):
    fishes = [starting]
    for _ in range(80):
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                fishes.append(9)
            else:
                fishes[i] = fish - 1
    total_after_80_days[starting] = len(fishes)

print(total_after_80_days)

# with open("tests/day6.txt", "r") as file:
with open("inputs/day6.txt", "r") as file:
    fishes = [int(num) for num in file.read().strip().split(",")]
    total = sum(total_after_80_days.get(fish) for fish in fishes)
    print(total)
