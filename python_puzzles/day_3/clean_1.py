size_example = "000000000000"
freq = [0] * len(size_example)
total = 0

with open("inputs/day3.txt", "r") as file:
    for line in file:
        for i, char in enumerate(line.strip()):
            if char == "1":
                freq[i] += 1
        total += 1

print(freq)
print(total)

gamma = ""
epsilon = ""
for count in freq:
    if (count/total) > 0.5:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma)
print(epsilon)
result = int(gamma, 2) * int(epsilon, 2)
print(result)
