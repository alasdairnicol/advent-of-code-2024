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


def find_path_to_end_2(points, start):
    initial_position = (start, (1, 0))  # starting square facing east
    seen = {initial_position: 0}
    best_paths = {initial_position: {(start,)}}
    queue = set([initial_position])

    while queue:
        (position, direction) = queue.pop()
        cost = seen[position, direction]
        paths = best_paths[position, direction]

        for new_position, new_direction, new_cost in next_states(
            position, direction, cost
        ):
            # print("considering", new_position, new_direction, new_cost)
            if new_position not in points:
                continue
            # print("considering", new_position, new_direction, )
            # if it's a new low, replace the existing paths
            # if it's equal add the paths
            # otherwise skip
            current_cost = seen.get((new_position, new_direction), new_cost + 1)
            if current_cost < new_cost:
                continue

            if current_cost > new_cost:
                # Clear the existing paths because we've found a better one
                best_paths[new_position, new_direction] = set()
                seen[(new_position, new_direction)] = new_cost

            best_paths[new_position, new_direction] |= {
                x + (new_position,) for x in paths
            }
            queue.add((new_position, new_direction))

    return best_paths


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

    best_paths = find_path_to_end_2(points, start)
    paths = [v for k, v in best_paths.items() if k[0] == end]
    points = set()
    for ppp in paths:
        for pp in ppp:
            for p in pp:
                points.add(p)

    part_2 = len(points)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day16.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
