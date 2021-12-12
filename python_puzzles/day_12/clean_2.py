class Cave:
    def __init__(self, name: str):
        # super().__init__(name)
        self.name = name
        self.is_large = name.isupper()
        self.connections = set()

    def connect(self, other: 'Cave'):
        self.connections.add(other)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


class System:
    def __init__(self, nodes: dict[str, Cave]):
        self.nodes = nodes

    def make_paths(self):
        start = self.nodes.get("start")
        visited = set()
        self.explore_paths((start,), start, visited)
        return visited

    def explore_paths(self, path: tuple[Cave, ...], node: Cave, visited: set[tuple]):
        # for new_path in ((*path, connection) for connection in node.connections):
        for connection in node.connections:
            new_path = (*path, connection)
            # if new_path not in visited:
            # if ((connection.is_large) or (connection not in path)) and (new_path not in visited):
            if self.validate_path(new_path):
                visited.add(new_path)
                if connection.name != "end":
                    self.explore_paths(new_path, connection, visited)

    def validate_path(self, path: tuple[Cave, ...]) -> bool:
        has_double_small = False
        for cave in set(path):
            if not cave.is_large:
                c = path.count(cave)
                if c > 2:
                    return False
                elif c == 2:
                    if has_double_small or (cave.name in ("start", "end")):
                        return False
                    else:
                        has_double_small = True
        return True


# with open("tests/day12_2.txt", "r") as file:
with open("inputs/day12.txt", "r") as file:
    nodes = {}
    for line in file:
        left, right = line.strip().split("-")
        if left not in nodes:
            nodes[left] = Cave(left)
        left = nodes.get(left)
        if right not in nodes:
            nodes[right] = Cave(right)
        right = nodes.get(right)
        left.connect(right)
        right.connect(left)
system = System(nodes)
paths = system.make_paths()
paths = {path for path in paths if path[-1].name == "end"}
print(len(paths))
# print(*paths, sep="\n")
