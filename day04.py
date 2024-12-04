#!/usr/bin/env python
from typing import Literal, cast

XmasLetter = Literal["X", "M", "A", "S"]
Grid = dict[tuple[int, int], XmasLetter]


def make_grid(lines: list[str]) -> Grid:
    grid = {
        (i, j): letter
        for j, line in enumerate(lines)
        for i, letter in enumerate(line)
        if letter in ["X", "M", "A", "S"]
    }
    return cast(Grid, grid)


def count_words_at_position(grid: Grid, x: int, y: int) -> int:
    count = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for distance, letter in enumerate("XMAS"):
                if grid.get((x + distance * i, y + distance * j)) != letter:
                    break
            else:
                count += 1
    return count


def do_part_1(grid: Grid) -> int:
    return sum(count_words_at_position(grid, x, y) for x, y in grid)


def is_xmas_at_position(grid: Grid, x: int, y: int) -> bool:
    return (
        grid[(x, y)] == "A"
        and sorted([grid.get((x + 1, y + 1), ""), grid.get((x - 1, y - 1), "")])
        == ["M", "S"]
        and sorted([grid.get((x + 1, y - 1), ""), grid.get((x - 1, y + 1), "")])
        == ["M", "S"]
    )


def do_part_2(grid: Grid) -> int:
    return sum(is_xmas_at_position(grid, x, y) for x, y in grid)


def main():
    lines = read_input()
    grid = make_grid(lines)

    part_1 = do_part_1(grid)
    print(f"{part_1=}")

    part_2 = do_part_2(grid)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day04.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
