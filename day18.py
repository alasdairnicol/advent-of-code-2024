#!/usr/bin/env python
Point = tuple[int, int]
Grid = set[Point]


def make_grid(lines: list[str], turns: int) -> Grid:
    return {
        (int(x), int(y)) for line in lines[:turns] for x, y in [line.strip().split(",")]
    }


def find_length_of_shortest_path(grid: Grid, start: Point, end: Point) -> int | None:
    queue = {start}
    best: dict[Point, int] = {start: 0}
    while queue:
        position = queue.pop()
        val = best[position] + 1
        # print("checking", position, val)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_pos = position[0] + dx, position[1] + dy
            if not (
                start[0] <= new_pos[0] <= end[0] and (start[1] <= new_pos[1] <= end[1])
            ):
                continue
            if new_pos in grid:
                continue
            if new_pos not in best or best[new_pos] > val:
                queue.add(new_pos)
                best[new_pos] = val
    return best.get(end)


def main() -> None:

    lines = read_input()

    start = (0, 0)
    end = (70, 70)
    turns = 1024
    grid = make_grid(lines, turns)
    print(grid)

    part_1 = find_length_of_shortest_path(grid, start, end)
    print(f"{part_1=}")

    part_2 = ""
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day18.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
