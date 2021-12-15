import itertools

import networkx as nx

graph = nx.Graph()


def get_values(file):
    for y, line in enumerate(file):
        for x, value in enumerate(line.strip()):
            yield x, y, value


def get_scaled_values(file):
    content = [thing for thing in file]
    offset_y = 0
    for scale_y, lines in enumerate(itertools.repeat(content, 5)):
        for pos_y, line in enumerate(lines):
            offset_x = 0
            for scale_x, values in enumerate(itertools.repeat(line.strip(), 5)):
                for pos_x, value in enumerate(values):
                    yield ((pos_x + offset_x), (pos_y + offset_y), (((int(value) + scale_x + scale_y) - 1) % 9) + 1)
                offset_x += pos_x + 1
            # print(offset_y, pos_y)
        # print(offset_y, pos_y)
        offset_y += pos_y + 1
        # print(offset_y, pos_y)


# list(itertools.repeat((thing for thing in range(3)), 3))

# with open("tests/day15.txt", "r") as file:
#     print(max(get_scaled_values(file), key = lambda tup: tup[0]))
# with open("tests/day15.txt", "r") as file:
    # print(max(get_scaled_values(file), key = lambda tup: tup[1]))

# with open("tests/day15_1.txt", "r") as file:
# with open("tests/day15.txt", "r") as file:
with open("inputs/day15.txt", "r") as file:
    # for x, y, value in get_values(file):
    for x, y, value in get_scaled_values(file):
        cur = (x, y)
        graph.add_node(cur, weight=int(value))
        if x > 0:
            graph.add_edge((x-1, y), cur)
        if y > 0:
            graph.add_edge((x, y-1), cur)

max_x, max_y = x, y

# max_x, max_y

path = nx.shortest_path(
    graph,
    source = (0, 0),
    target = (max_x, max_y),
    weight = lambda n1, n2, e: graph.nodes[n1]["weight"]+graph.nodes[n2]["weight"]
)


# def display(p):
#     result = ""
#     for y in range(max_x):
#         for x in range(max_y):
#             if (x, y) in path:
#                 result += "#"
#             else:
#                 result += " "
#         result += "\n"
#     return result
#
#
# print(display(path))
print(sum(graph._node[node]["weight"] for node in path[1:]))
