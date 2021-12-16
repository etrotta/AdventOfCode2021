import operator
import functools

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

op_map = {
    0: lambda *xs: functools.reduce(operator.add, xs, 0),
    1: lambda *xs: functools.reduce(operator.mul, xs, 1),
    2: lambda *xs: functools.reduce(min, xs, float('inf')),
    3: lambda *xs: functools.reduce(max, xs, float('-inf')),
    5: operator.gt,
    6: operator.lt,
    7: operator.eq,
}


def hex_to_bin(string: str) -> str:
    return "".join(hex_map.get(char) for char in string)


def buffer(content: str):
    "Generator that allows for you to request N characters."
    it = iter(content)
    n = yield None
    while True:
        cur = ""
        for _ in range(n):
            cur += next(it)
        n = yield cur


class Parser:
    def __init__(self, content: str):
        self.traceback = []
        self.buffer = buffer(content)
        self.buffer.send(None)
        self.total_bits = 0

    def consume(self, count: int) -> str:
        # print(count)
        self.total_bits += count
        return self.buffer.send(count)

    def next(self):
        # print("Package Start")
        version_number = int(self.consume(3), 2)
        type_id = int(self.consume(3), 2)
        if type_id == 4:  # Literal
            result = ""
            while True:
                group = self.consume(5)
                result += group[1:]
                if group[0] == "0":
                    break
            result = int(result, 2)
            return result
        else:  # Operator
            length_mode = self.consume(1)
            if length_mode == "0":
                # 15 bits - total number of bits in this group
                length = int(self.consume(15), 2)
                old = self.total_bits
                packages = []
                while (old + length) > self.total_bits:
                    packages.append(self.next())
                # return (type_id, packages)
                # print(type_id, packages)
                return op_map[type_id](*packages)
            else:
                # 11 bits - number of sub-packages in this one
                length = int(self.consume(11), 2)
                packages = [self.next() for _ in range(length)]
                # return (type_id, packages)
                # print(type_id, packages)
                return op_map[type_id](*packages)


if __name__ == "__main__":
    with open("inputs/day16.txt", "r") as file:
        content = hex_to_bin(file.read().strip())
        parser = Parser(content)
        print(parser.next())
