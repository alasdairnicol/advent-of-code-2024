#!/usr/bin/env python
Point = tuple[int, int]


next_directions: dict[Point, Point] = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}


def find_obstructions(lines: list[str]) -> set[Point]:
    return {
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line)
        if val == "#"
    }


def find_guard(lines: list[str]) -> Point:
    return next(
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line)
        if val == "^"
    )


def find_path(
    obstructions: set[Point], guard: Point, direction: Point, width: int, height: int
) -> set[Point]:
    visited = set()
    while 0 <= guard[0] < width and 0 <= guard[1] < height:
        visited.add(guard)

        ahead = (guard[0] + direction[0], guard[1] + direction[1])
        if ahead not in obstructions:
            guard = ahead
        else:
            direction = next_directions[direction]

    return visited


def do_part_2(
    initial_obstructions, visited, initial_guard, initial_direction, width, height
) -> int:
    count = 0
    for block in visited ^ {initial_guard}:
        obstructions = initial_obstructions | {block}
        guard = initial_guard
        direction = initial_direction
        seen = set()
        while True:
            if not (0 <= guard[0] < width and 0 <= guard[1] < height):
                break
            elif (guard, direction) in seen:
                # loop detected
                count += 1
                break

            seen.add((guard, direction))
            ahead = (guard[0] + direction[0], guard[1] + direction[1])
            if ahead not in obstructions:
                guard = ahead
            else:
                direction = next_directions[direction]
    return count


def main():
    lines = read_input()
    obstructions = find_obstructions(lines)
    guard = find_guard(lines)
    width = len(lines[0].strip())
    height = len(lines)
    direction = (0, -1)

    visited = find_path(obstructions, guard, direction, width, height)
    part_1 = len(visited)

    print(f"{part_1=}")

    part_2 = do_part_2(obstructions, visited, guard, direction, width, height)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day06.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
