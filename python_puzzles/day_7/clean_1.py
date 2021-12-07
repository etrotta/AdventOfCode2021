import statistics

# with open("tests/day7.txt", "r") as file:
with open("inputs/day7.txt", "r") as file:
    numbers = [int(n) for n in file.read().strip().split(",")]
    numbers.sort()
    # print(numbers)

    medi = statistics.median(numbers)
    print(medi)

    fuel = sum(abs(pos - medi) for pos in numbers)
    print(fuel)
