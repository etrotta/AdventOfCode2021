import numpy as np
import matplotlib.pyplot as plt

# with open("tests/day7.txt", "r") as file:
with open("inputs/day7.txt", "r") as file:
    numbers = np.array(sorted(int(n) for n in file.read().strip().split(",")))


# def cost_p1(arr, x):
    # return np.sum(np.abs(arr - x))


def cost(arr, x):
    tmp = np.abs(arr - x)
    return np.sum((np.power(tmp, 2) + tmp) / 2)


xs = []
ys = []
for final in range(1000):
    xs.append(final)
    ys.append(cost(numbers, final))

plt.plot(xs, ys)
plt.plot(xs[400:600], ys[400:600])
plt.plot(xs[475:525], ys[475:525])
print(min(ys), ys.index(min(ys)))
