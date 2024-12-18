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


def has_path(lines: list[str], start: Point, end: Point, turns: int):
    grid = make_grid(lines, turns=turns)
    return find_length_of_shortest_path(grid, start, end) is not None


def do_part_1(lines: list[str], start: Point, end: Point) -> int:
    grid = make_grid(lines, 1024)
    length = find_length_of_shortest_path(grid, start, end)
    assert length is not None
    return length


def do_part_2(lines: list[str], start: Point, end: Point) -> str:
    low = 1024
    high = len(lines)
    while high - low > 1:
        guess = (low + high) // 2
        if has_path(lines, start, end, guess):
            low = guess
        else:
            high = guess
    # The high'th entry is at index high - 1
    return lines[high - 1].strip()


def main() -> None:

    lines = read_input()

    start = (0, 0)
    end = (70, 70)

    part_1 = do_part_1(lines, start, end)
    print(f"{part_1=}")

    part_2 = do_part_2(lines, start, end)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day18.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
