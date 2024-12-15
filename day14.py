#!/usr/bin/env python
from collections import Counter
import math

Guard = tuple[int, int, int, int]


def parse_line(line: str) -> tuple[int, int, int, int]:
    p, v = line.split()
    x, y = (int(x) for x in p[2:].split(",", maxsplit=1))
    vx, vy = (int(x) for x in v[2:].split(",", maxsplit=1))
    return x, y, vx, vy


def find_position(
    guard: Guard,
    width: int,
    height: int,
    turns: int = 1,
) -> Guard:
    x, y, vx, vy = guard
    return (x + turns * vx) % width, (y + turns * vy) % height, vx, vy


def do_part_1(guards: list[Guard], width: int, height: int) -> int:
    final_positions = Counter(
        find_position(guard, width, height, turns=100)[:2] for guard in guards
    )
    final_positions.items()
    quadrants = [
        sum(
            v
            for (x, y), v in final_positions.items()
            if x < width // 2 and y < height // 2
        ),
        sum(
            v
            for (x, y), v in final_positions.items()
            if x > width // 2 and y < height // 2
        ),
        sum(
            v
            for (x, y), v in final_positions.items()
            if x < width // 2 and y > height // 2
        ),
        sum(
            v
            for (x, y), v in final_positions.items()
            if x > width // 2 and y > height // 2
        ),
    ]
    return math.prod(quadrants)


def main():
    lines = read_input()

    width = 101
    height = 103

    guards = [parse_line(line) for line in lines]
    part_1 = do_part_1(guards, width, height)
    print(f"{part_1=}")

    part_2 = "???"
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day14.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
