def step(numbers: list[str], index: int, rule) -> int:
    if len(numbers) == 1:
        return numbers[0]
    zero_count = 0
    one_count = 0
    for number in numbers:
        if number[index] == "0":
            zero_count += 1
        else:
            one_count += 1
    desired = str(int(rule(zero_count, one_count)))
    accepted = []
    for number in numbers:
        if number[index] == desired:
            accepted.append(number)
    return step(accepted, index + 1, rule)


numbers: list[str] = []
# with open("tests/day3.txt", "r") as file:
with open("inputs/day3.txt", "r") as file:
    for line in file:
        numbers.append(line.strip())


yes = step(numbers, 0, lambda zero_count, one_count: zero_count <= one_count)
no = step(numbers, 0, lambda zero_count, one_count: zero_count > one_count)
result = int(yes, 2) * int(no, 2)
print(yes, int(yes, 2))
print(no, int(no, 2))
print(result)
