def step(numbers, index, rule):
    if len(numbers) == 1:
        return "".join(numbers[0])
    d = rule(sum(((n[index] == "1")*2)-1 for n in numbers))
    return step([n for n in numbers if n[index] == d], index + 1, rule)


with open("inputs/day3.txt", "r") as file:
    numbers = [list(line.strip()) for line in file]

yes = step(numbers, 0, lambda num: "1" if num >= 0 else "0")  # oxygen
no = step(numbers, 0, lambda num: "1" if num < 0 else "0")  # co2
result = int(yes, 2) * int(no, 2)
print(result)
