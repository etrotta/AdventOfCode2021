# total_after_256_days = {}
# for starting in range(1, 7):
#     fishes = [starting]
#     for _ in range(256):
#         print(len(fishes))
#         for i, fish in enumerate(fishes):
#             if fish == 0:
#                 fishes[i] = 6
#                 fishes.append(9)
#             else:
#                 fishes[i] = fish - 1
#     total_after_256_days[starting] = len(fishes)

# print(total_after_256_days)

# with open("inputs/day6.txt", "r") as file:
answer = 26984457539

value = 26984457539 // 5

with open("tests/day6.txt", "r") as file:
    fishes = [int(num) for num in file.read().strip().split(",")]

for offset in range(-100, 100):
    total_after_256_days = {
        fish: value - offset + ((256 % 7 // fish))
        for fish in range(1, 7)
    }
    total = sum(total_after_256_days.get(fish) for fish in fishes)
    if total == answer:
        print("FUCK YES")
        print(offset)
        print(total)
        break
else:
    print("fuck no")

print(total_after_256_days)
# if it works it works

with open("inputs/day6.txt", "r") as file:
    fishes = [int(num) for num in file.read().strip().split(",")]

yeet = sum(total_after_256_days.get(fish) for fish in fishes)
print(yeet)

# oof too low
# ...yeah assuming that it was evenly distributed was a dumb move
