#!/usr/bin/env python
import collections
import itertools

Point = tuple[int, int]
Grid = set[Point]
Distances = dict[Point, int]


def make_grid(lines: list[str]) -> Grid:
    return {
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val != "#"
    }


def find_path(grid: Grid, start: Point) -> Distances:
    distances: dict[Point, int] = {start: 0}
    queue = collections.deque([start])

    while queue:
        x, y = queue.popleft()
        distance = distances[x, y]
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            point = (x + dx, y + dy)
            if point in grid and point not in distances:
                distances[point] = distance + 1
                queue.append(point)
    return distances


def find_two_stepshortcuts(distances: Distances, point: Point):
    # for part 1
    x, y = point
    distance = distances[point]
    for dx, dy in ((2, 0), (0, 2), (-2, 0), (0, -2)):
        point_2 = (x + dx, y + dy)
        if point_2 in distances:
            saved = distances[point_2] - distance - 2
            if saved > 0:
                yield saved


def do_part_1(distances) -> int:
    shortcuts = []
    for point in distances:
        for shortcut in find_two_stepshortcuts(distances, point):
            shortcuts.append(shortcut)
    return len([x for x in shortcuts if x >= 100])


def do_part_2(distances) -> int:
    count = 0
    for (sx, sy), (ex, ey) in itertools.combinations(distances, 2):
        saving = abs(distances[ex, ey] - distances[sx, sy]) - (
            abs(ex - sx) + abs(ey - sy)
        )
        if saving >= 100 and (abs(ex - sx) + abs(ey - sy)) <= 20:
            count += 1
    return count


def main() -> None:
    lines = read_input()

    grid = make_grid(lines)
    start = next(
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val == "S"
    )

    distances = find_path(grid, start)

    part_1 = do_part_1(distances)
    print(f"{part_1=}")

    part_2 = do_part_2(distances)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day20.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
