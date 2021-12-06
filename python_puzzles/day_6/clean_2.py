total_after_256_days = {}
for starting in range(1, 7):
    fishes = {i: 0 for i in range(10)}
    nxt = {i: 0 for i in range(10)}
    fishes[starting] = 1
    for _ in range(256):
        for i, count in fishes.items():
            # print(i, count)
            if i == 0:
                nxt[7-1] += count
                nxt[9-1] += count
            else:
                nxt[i - 1] += count
        # print(nxt)
        fishes = nxt
        nxt = {i: 0 for i in range(10)}
    # print(fishes)
    total_after_256_days[starting] = sum(fishes.values())
    # break

# print('Expected: ', "{1: 1401, 2: 1191, 3: 1154, 4: 1034, 5: 950, 6: 905}")
print('Received: ', total_after_256_days)

# with open("tests/day6.txt", "r") as file:
with open("inputs/day6.txt", "r") as file:
    fishes = [int(num) for num in file.read().strip().split(",")]
    total = sum(total_after_256_days.get(fish) for fish in fishes)
    print(total)
