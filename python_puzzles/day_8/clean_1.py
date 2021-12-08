# with open("tests/day8.txt", "r") as file:
with open("inputs/day8.txt", "r") as file:
    total = 0
    for line in file:
        inputs, outputs = line.split("|")
        for output in outputs.split():
            if len(output.strip()) in (2, 4, 3, 7):
                total += 1
    print(total)
