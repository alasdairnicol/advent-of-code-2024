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
    # This is a very specific solution that works for my input.
    # I saw that every node was connected to 13 other nodes
    # That would give a maximum possible clique size of 14
    # By inspection, I could see a clique of 12.
    # Therefore my solution could brute force through the possible
    # cliques of 14 and 13 until it found one.
    assert [len(v) == 13 for v in connections]
    for clique_size in range(14, 0, -1):
        for c, v in connections.items():
            for nodes in itertools.combinations(v | {c}, clique_size):
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
