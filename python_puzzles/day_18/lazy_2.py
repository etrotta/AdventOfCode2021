from ast import literal_eval
from .octi_num import PairNumber


def combinations(seq):
    for element in seq:
        for other in seq:
            if element is not other:
                yield element, other


numbers = []

# with open("tests/day18.txt", "r") as file:
with open("inputs/day18.txt", "r") as file:
    for line in file:
        line = literal_eval(line.strip())
        numbers.append(line)
        # number = PairNumber.from_list(line, None)
        # while number.check_explode() or number.check_split():
        #     pass
        # numbers.append(number)


def get_score(numbers):
    n1, n2 = numbers
    # In retrospect:
    # I kinda wish I had done it in a way that supports immutability but yeah...
    # it is easier to just generate them each time instead
    n1 = PairNumber.from_list(n1, None)
    n2 = PairNumber.from_list(n2, None)
    result = n1.add(n2)
    while result.check_explode() or result.check_split():
        pass
    return result.get_magnitude()


best = max(combinations(numbers), key = get_score)
print(best)
print(get_score(best))
