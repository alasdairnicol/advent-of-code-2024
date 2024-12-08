#!/usr/bin/env python
from collections import defaultdict
import itertools

Point = tuple[int, int]
Grid = dict[str, list[Point]]


def parse_grid(lines: list[str]) -> Grid:
    grid = defaultdict(list)
    for j, line in enumerate(lines):
        for i, val in enumerate(line.strip()):
            if val != ".":
                grid[val].append((i, j))
    return grid


def antinodes_for_pair(point_a, point_b):
    return {
        (2 * point_a[0] - point_b[0], 2 * point_a[1] - point_b[1]),
        (2 * point_b[0] - point_a[0], 2 * point_b[1] - point_a[1]),
    }


def antinodes_for_pair_2(point_a, point_b, width, height):
    delta = (point_b[0] - point_a[0], point_b[1] - point_a[1])
    yield point_a

    point = point_a
    while True:
        if not (0 <= point[0] < width and 0 <= point[1] < height):
            break
        yield point
        point = point[0] + delta[0], point[1] + delta[1]
    # extend the other way
    point = point_a
    while True:
        if not (0 <= point[0] < width and 0 <= point[1] <= height):
            break
        yield point
        point = point[0] - delta[0], point[1] - delta[1]


def do_part_1(grid: Grid, width: int, height: int) -> int:
    antinodes = set()
    for antennas in grid.values():
        for point_a, point_b in itertools.combinations(antennas, 2):
            antinodes |= antinodes_for_pair(point_a, point_b)
    return len([a for a in antinodes if 0 <= a[0] < width and 0 <= a[1] < height])


def do_part_2(grid: Grid, width: int, height: int) -> int:
    antinodes = set()
    for antennas in grid.values():
        for point_a, point_b in itertools.combinations(antennas, 2):
            antinodes |= set(antinodes_for_pair_2(point_a, point_b, width, height))
    return len(antinodes)


def main():
    lines = read_input()
    grid = parse_grid(lines)
    width = len(lines[0].strip())
    height = len(lines)
    print(grid)

    part_1 = do_part_1(grid, width, height)
    print(f"{part_1=}")

    part_2 = do_part_2(grid, width, height)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day08.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
