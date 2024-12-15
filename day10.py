#!/usr/bin/env python

Point = tuple[int, int]
Grid = dict[Point, int]


def parse_grid(lines: list[str]) -> Grid:
    return {
        (i, j): int(val)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
    }


def trailhead_score_part_1(grid: Grid, point: Point) -> int:
    queue = [point]
    count = 0
    visited = set()
    while queue:
        point = queue.pop()
        if (val := grid.get(point)) is not None:
            visited.add(point)
            if val == 9:
                count += 1
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                neighbour = point[0] + dx, point[1] + dy
                if (
                    neighbour in grid
                    and neighbour not in visited
                    and (grid[neighbour] - val) == 1
                ):
                    queue.append(neighbour)
    return count


def trailhead_score_part_2(grid: Grid, point: Point) -> int:
    queue: list[tuple[Point, ...]] = [(point,)]
    count = 0
    visited = set()
    while queue:
        trail = queue.pop()
        point = trail[-1]
        if (val := grid.get(point)) is not None:
            visited.add(point)
            if val == 9:
                count += 1
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                neighbour = point[0] + dx, point[1] + dy
                new_trail = trail + (neighbour,)
                if (
                    neighbour in grid
                    and new_trail not in visited
                    and (grid[neighbour] - val) == 1
                ):
                    queue.append(new_trail)
    return count


def main() -> None:
    lines = read_input()
    grid = parse_grid(lines)
    zeroes = [k for k, v in grid.items() if v == 0]

    part_1 = sum(trailhead_score_part_1(grid, point) for point in zeroes)
    print(f"{part_1=}")

    part_2 = sum(trailhead_score_part_2(grid, point) for point in zeroes)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day10.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
