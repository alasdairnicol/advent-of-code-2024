#!/usr/bin/env python
import itertools
from collections import defaultdict

Connections = dict[str, set[str]]


def parse_lines(lines: list[str]) -> Connections:
    connections = defaultdict(set)
    for line in lines:
        node_a, node_b = line.strip().split("-")
        connections[node_a].add(node_b)
        connections[node_b].add(node_a)
    return connections


def is_fully_connected(connections: Connections, nodes: tuple[str, ...]):
    for a, b in itertools.combinations(nodes, 2):
        if b not in connections[a]:
            return False
    return True


def do_part_1(connections: Connections) -> int:
    found = set()
    for c in connections:
        if c.startswith("t"):
            for a, b in itertools.combinations(connections[c], 2):
                if b in connections[a]:
                    found.add(tuple(sorted((a, b, c))))
    return len(found)


def do_part_2(connections: Connections) -> str:
    num_connections = 13
    assert [len(v) == num_connections for v in connections]
    for c, v in connections.items():
        for nodes in itertools.combinations(v | {c}, num_connections):
            if is_fully_connected(connections, nodes):
                return ",".join(sorted(nodes))

    # Shouldn't ever get here
    raise ValueError


def main() -> None:
    lines = read_input()

    connections = parse_lines(lines)

    part_1 = do_part_1(connections)
    print(f"{part_1=}")

    part_2 = do_part_2(connections)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day23.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
