# import octi_num
from .octi_num import PairNumber

test_case = [
    [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
    [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
    [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
    [7, [5, [[3, 8], [1, 4]]]],
    [[2, [2, 2]], [8, [8, 1]]],
    [2, 9],
    [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
    [[[5, [7, 4]], 7], 1],
    [[[[4, 2], 2], 6], [8, 7]],
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
