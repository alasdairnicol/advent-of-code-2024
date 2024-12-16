#!/usr/bin/env python

Point = tuple[int, int]


def make_points(lines: list[str]) -> set[Point]:
    return set(
        [
            (i, j)
            for j, line in enumerate(lines)
            for i, val in enumerate(line.strip())
            if val != "#"
        ]
    )


def next_states(position, direction, cost):
    x, y = position
    dx, dy = direction

    yield ((x + dx, y + dy), (dx, dy), cost + 1)  # forward
    yield ((x, y), (-dy, dx), cost + 1000)  # turn clockwise
    yield ((x, y), (dy, -dx), cost + 1000)  # turn anticlockwise


def find_path_to_end(points, start):
    initial_position = (start, (1, 0))  # starting square facing east
    seen = {initial_position: 0}
    queue = set([initial_position])

    while queue:
        (position, direction) = queue.pop()
        cost = seen[position, direction]

        for new_position, new_direction, new_cost in next_states(
            position, direction, cost
        ):
            if new_position not in points:
                continue
            # print("considering", new_position, new_direction, )
            if seen.get((new_position, new_direction), new_cost + 1) > new_cost:
                seen[(new_position, new_direction)] = new_cost
                queue.add((new_position, new_direction))

    return seen


def main() -> None:
    lines = read_input()

    points = make_points(lines)
    start = next(
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val == "S"
    )
    end = next(
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val == "E"
    )

    seen = find_path_to_end(points, start)

    part_1 = min(v for k, v in seen.items() if k[0] == end)
    print(f"{part_1=}")

    part_2 = ""
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day16.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
