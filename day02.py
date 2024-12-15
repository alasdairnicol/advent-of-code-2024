#!/usr/bin/env python
import itertools


def cmp(x: int, y: int) -> int:
    return (x > y) - (x < y)


def parse_line(line) -> list[int]:
    return [int(x) for x in line.split()]


def check_line(line: list[int]) -> bool:
    return (
        all(1 <= abs(x - y) <= 3 for x, y in itertools.pairwise(line))
        and len(set(cmp(x, y) for x, y in itertools.pairwise(line))) == 1
    )


def check_line_with_tolerance(line: list[int]) -> bool:
    """
    Generate every possible trial_line that excludes one item

    If any of these trial_lines is valid, then the line passes.

    It's a bit inefficient to check the entire trial_line, rather
    than going through the line and counting the bad levels, but
    this way we don't have to keep track of state.
    """
    for x in range(len(line)):
        trial_line = line[:x] + line[x + 1 :]
        if check_line(trial_line):
            return True

    return False


def do_part_1(lines: list[list[int]]) -> int:
    return sum(check_line(line) for line in lines)


def do_part_2(lines: list[list[int]]) -> int:
    return sum(check_line_with_tolerance(line) for line in lines)


def main() -> None:
    lines = [parse_line(line) for line in read_input()]

    part_1 = do_part_1(lines)
    print(f"{part_1=}")

    part_2 = do_part_2(lines)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day02.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
