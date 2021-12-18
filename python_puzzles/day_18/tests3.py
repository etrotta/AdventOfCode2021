# import octi_num
from .octi_num import PairNumber

test_case = [
    [[[[4, 3], 4], 4], [7, [[8, 4], 9]]],
    [1, 1],
]
# expected_result = "[[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]"
# expected_mag = 4140

lines = iter(test_case)
result = PairNumber.from_list(next(lines), parent=None)

for line in lines:
    result = result.add(PairNumber.from_list(line, None))
    print(result)
    while result.check_explode() or result.check_split():
        # the checks do operations on their own
        print(result)
        pass
# assert str(result) == expected_result
# assert result.get_magnitude() == expected_mag
