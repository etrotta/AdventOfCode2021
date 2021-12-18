from ast import literal_eval
from .octi_num import PairNumber

# with open("tests/day18.txt", "r") as file:
with open("inputs/day18.txt", "r") as file:
    result = PairNumber.from_list(literal_eval(next(file).strip()), None)
    for line in file:
        line = literal_eval(line.strip())
        other = PairNumber.from_list(line, None)
        result = result.add(other)
        while result.check_explode() or result.check_split():
            pass
    print(result)
    print(result.get_magnitude())
