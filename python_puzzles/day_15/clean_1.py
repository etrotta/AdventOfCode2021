import networkx as nx

graph = nx.Graph()

# with open("tests/day15_1.txt", "r") as file:
# with open("tests/day15.txt", "r") as file:
with open("inputs/day15.txt", "r") as file:
    for y, line in enumerate(file):
        for x, value in enumerate(line.strip()):
            cur = (x, y)
            graph.add_node(cur, weight=int(value))
            if x > 0:
                graph.add_edge((x-1, y), cur)
            if y > 0:
                graph.add_edge((x, y-1), cur)

max_x, max_y = x, y

path = nx.shortest_path(graph, source = (0, 0), target = (max_x, max_y), weight=lambda n1, n2, e: graph.nodes[n1]["weight"]+graph.nodes[n2]["weight"])


def display(p):
    result = ""
    for y in range(max_x):
        for x in range(max_y):
            if (x, y) in path:
                result += "#"
            else:
                result += " "
        result += "\n"
    return result


print(display(path))
print(sum(graph._node[node]["weight"] for node in path[1:]))
