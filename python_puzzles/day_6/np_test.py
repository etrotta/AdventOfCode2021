import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

with open("python_puzzles/day_6/test.txt", "r") as file:
    lines = np.log(np.array([int(num) for num in file]))
    n_lines = len(lines)
    X = list(range(n_lines))

# model = poly.Polynomial.fit(X, lines, 2)
# model
# dir(model)
model = poly.polyfit(X, lines, 2)
predicted = poly.polyval(X, model)
# model(80)
# lines[80]

plt.plot(predicted)
plt.plot(lines)

plt.plot(lines - predicted)

plt.plot(np.exp(lines))
plt.plot(np.exp(lines[:20]))
