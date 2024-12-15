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


def find_mean_point(guards: list[Guard]) -> tuple[float, float]:
    return (
        sum(guard[0] for guard in guards) / len(guards),
        sum(guard[1] for guard in guards) / len(guards),
    )


def sum_square_distances(guards: list[Guard]) -> float:
    mean = find_mean_point(guards)
    return sum(
        (guard[0] - mean[0]) ** 2 + (guard[1] - mean[1]) ** 2 for guard in guards
    )


def do_part_2(guards: list[Guard], width: int, height: int) -> int:
    # I originally found the solution by generating bitmaps and eyeballing the images
    # This approach of minimising the square distance is thanks to Reddit
    original_guards = guards[:]
    total_square_distances: dict[int, float] = {}
    for i in range(1, width * height + 1):
        guards = [find_position(guard, width, height) for guard in guards]
        total_square_distances[i] = sum_square_distances(guards)

    # We're back in the original position. No point checking any further
    # Credit to @jamienicol for predicting it would cycle every width*height turns
    assert guards == original_guards

    # Return the key with the small sum of square distances
    return sorted(total_square_distances, key=lambda k: total_square_distances[k])[0]


def main():
    lines = read_input()

    width = 101
    height = 103

    guards = [parse_line(line) for line in lines]
    part_1 = do_part_1(guards, width, height)
    print(f"{part_1=}")

    part_2 = do_part_2(guards, width, height)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day14.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
