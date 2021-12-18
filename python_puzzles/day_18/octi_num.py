# from ast import literal_eval
from typing import Union
from abc import ABC, abstractmethod
from math import ceil, floor


class OctiNumber(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def get_outer_left(self):
        "Returns the closest OctiNumber to the Left of this one, that does not contains it."
        if self.parent is None:
            return None
        if self.parent.left is self:
            return self.parent.get_outer_left()
        else:
            return self.parent.left

    def get_outer_right(self):
        "Returns the closest OctiNumber to the Right of this one, that does not contains it."
        if self.parent is None:
            return None
        if self.parent.right is self:
            return self.parent.get_outer_right()
        else:
            return self.parent.right

    @abstractmethod
    def get_inner_left(self):
        "Returns leftmost OctiNumber contained within this one."
        pass

    @abstractmethod
    def get_inner_right(self):
        "Returns rightmost OctiNumber contained within this one."
        pass

    @abstractmethod
    def check_explode(self):
        pass

    @abstractmethod
    def get_magnitude(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class PairNumber(OctiNumber):
    def __init__(self, left: OctiNumber, right: OctiNumber, parent: Union['PairNumber', None]):
        self.left = left
        self.right = right
        self.parent = parent

    @classmethod
    def from_list(cls, lst, parent: Union['PairNumber', None]) -> 'PairNumber':
        self = cls(None, None, parent)
        left, right = lst

        if isinstance(left, int):
            left = SingleNumber(left, self)
        elif isinstance(left, list):
            left = PairNumber.from_list(left, self)
        else:
            raise NotImplementedError
        self.left = left

        if isinstance(right, int):
            right = SingleNumber(right, self)
        elif isinstance(right, list):
            right = PairNumber.from_list(right, self)
        else:
            raise NotImplementedError
        self.right = right

        return self

    def get_inner_left(self) -> 'SingleNumber':
        return self.left.get_inner_left()

    def get_inner_right(self) -> 'SingleNumber':
        return self.right.get_inner_right()

    def do_explode(self) -> None:
        left = self.get_outer_left()
        if left is not None:
            left.get_inner_right().add(self.left)

        right = self.get_outer_right()
        if right is not None:
            right.get_inner_left().add(self.right)

    def check_explode(self, depth = 0) -> int:
        left = self.left.check_explode(depth + 1)
        if left == 2:
            self.left = SingleNumber(0, self)
            return 1
        elif left == 1:
            return 1

        right = self.right.check_explode(depth + 1)
        if right == 2:
            self.right = SingleNumber(0, self)
            return 1
        elif right == 1:
            return 1

        if depth >= 4:
            self.do_explode()
            return 2

        return 0

    def check_split(self) -> bool:
        if self.left.check_split():
            if isinstance(self.left, SingleNumber):
                self.left = self.left.do_split()
            return True
        if self.right.check_split():
            if isinstance(self.right, SingleNumber):
                self.right = self.right.do_split()
            return True
        return False

    def get_magnitude(self) -> int:
        return (self.left.get_magnitude() * 3) + (self.right.get_magnitude() * 2)

    def add(self, other: 'PairNumber') -> 'PairNumber':
        if not isinstance(other, PairNumber):
            raise NotImplementedError
        parent = PairNumber(self, other, self.parent)
        self.parent = parent
        other.parent = parent
        return parent

    def __repr__(self) -> str:
        return f"PairNumber([{repr(self.left)}, {repr(self.right)}])"

    def __str__(self) -> str:
        return f"[{str(self.left)}, {str(self.right)}]"


class SingleNumber(OctiNumber):
    def __init__(self, value: int, parent: PairNumber):
        self.value = value
        self.parent = parent

    def get_inner_left(self) -> 'SingleNumber':
        return self

    def get_inner_right(self) -> 'SingleNumber':
        return self

    def check_explode(self, depth) -> bool:
        return False

    def do_split(self) -> PairNumber:
        pn = PairNumber(None, None, self.parent)
        pn.left = SingleNumber(floor(self.value / 2), pn)
        pn.right = SingleNumber(ceil(self.value / 2), pn)
        return pn

    def check_split(self) -> bool:
        return self.value >= 10

    def get_magnitude(self) -> int:
        return self.value

    def add(self, other: 'SingleNumber') -> None:
        if not isinstance(other, SingleNumber):
            raise NotImplementedError
        self.value += other.value

    def __repr__(self) -> str:
        return f"SingleNumber({self.value})"

    def __str__(self) -> str:
        return f"{self.value}"


if __name__ == "__main__":
    print("Solo test")
    test = PairNumber.from_list([[[2, 3], 4], [5, [6, [[9, 1], 1]]]], parent = None)
    print(test)
    while test.check_explode() or test.check_split():
        print(test)
    print(test.get_magnitude())
    print("Addition test...")
    test2 = PairNumber.from_list([1, 1], parent = None)
    print(test)
    print(test2)
    print()
    test = test.add(test2)
    print(test)
    while test.check_explode() or test.check_split():
        print(test)
    print(test.get_magnitude())
