#!/usr/bin/env python
from collections import defaultdict
import itertools
import math

Point = tuple[int, int]
Grid = dict[str, list[Point]]


def parse_grid(lines: list[str]) -> Grid:
    grid = defaultdict(list)
    for j, line in enumerate(lines):
        for i, val in enumerate(line.strip()):
            if val != ".":
                grid[val].append((i, j))
    return grid


def in_bounds(point: Point, width: int, height: int):
    return 0 <= point[0] < width and 0 <= point[1] < height


def antinodes_for_pair_part_1(point_a: Point, point_b: Point, width: int, height: int):
    points = [
        (2 * point_a[0] - point_b[0], 2 * point_a[1] - point_b[1]),
        (2 * point_b[0] - point_a[0], 2 * point_b[1] - point_a[1]),
    ]
    for point in points:
        if in_bounds(point, width, height):
            yield point


def antinodes_for_pair_part_2(point_a: Point, point_b: Point, width: int, height: int):
    delta = (point_b[0] - point_a[0], point_b[1] - point_a[1])
    gcd = math.gcd(*delta)
    min_step = (delta[0] // gcd, delta[1] // gcd)
    yield point_a

    point = point_a
    while True:
        if not (0 <= point[0] < width and 0 <= point[1] < height):
            break
        yield point
        point = point[0] + min_step[0], point[1] + min_step[1]
    # extend the other way
    point = point_a
    while True:
        if not (0 <= point[0] < width and 0 <= point[1] <= height):
            break
        yield point
        point = point[0] - min_step[0], point[1] - min_step[1]


def count_antinodes(grid: Grid, width: int, height: int, antinodes_for_pair) -> int:
    antinodes = set()
    for antennas in grid.values():
        for point_a, point_b in itertools.combinations(antennas, 2):
            antinodes |= set(antinodes_for_pair(point_a, point_b, width, height))
    return len(antinodes)


def main():
    lines = read_input()
    grid = parse_grid(lines)
    width = len(lines[0].strip())
    height = len(lines)

    part_1 = count_antinodes(grid, width, height, antinodes_for_pair_part_1)
    print(f"{part_1=}")

    part_2 = count_antinodes(grid, width, height, antinodes_for_pair_part_2)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day08.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
