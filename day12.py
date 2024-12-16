#!/usr/bin/env python
import itertools
from collections import defaultdict
from typing import TypeVar

T = TypeVar("T")
Point = tuple[int, int]
Grid = dict[Point, T]


def num_neighbours_for_point(grid: Grid[str], point: Point) -> int:
    return len(
        [
            dx
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if grid.get((point[0] + dx, point[1] + dy)) != grid[point]
        ]
    )


def count_edges(edges_dict) -> int:
    total = 0
    for v in edges_dict.values():
        total += len([y for x, y in itertools.pairwise(sorted(v)) if x + 1 != y]) + 1
    return total


def fill_shape(
    grid: Grid[str], shape_sizes: Grid[int], shape_edges: Grid[int], point: Point
):
    value = grid[point]
    queue = set([point])
    shape = set()
    edges = defaultdict(list)
    while queue:
        (i, j) = queue.pop()
        shape.add((i, j))
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neighbour = (i + dx, j + dy)
            if grid.get(neighbour) == value:
                if neighbour in shape:
                    pass
                else:
                    queue.add(neighbour)
            else:
                if dx:
                    edges[dx, dy, i].append(j)
                else:
                    edges[dx, dy, j].append(i)
    size = len(shape)
    num_edges = count_edges(edges)
    for point in shape:
        shape_sizes[point] = size
        shape_edges[point] = num_edges


def main() -> None:
    lines = read_input()

    grid = {
        (i, j): val
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
    }

    neighbours_grid = {
        (i, j): num_neighbours_for_point(grid, (i, j))
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
    }

    shape_sizes: dict[Point, int] = {}
    shape_edges: dict[Point, int] = {}
    for point in grid:
        if point in shape_sizes:
            continue
        fill_shape(grid, shape_sizes, shape_edges, point)

    part_1 = sum(
        shape_size * neighbours_grid[point] for point, shape_size in shape_sizes.items()
    )
    print(f"{part_1=}")

    part_2 = sum(shape_edges.values())
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day12.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
