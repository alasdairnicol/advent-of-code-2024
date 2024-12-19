#!/usr/bin/env python
import functools


def parse_input(lines: list[str]) -> tuple[tuple[str, ...], list[str]]:
    towels = tuple(lines[0].strip().split(", "))
    patterns = [p.strip() for p in lines[2:]]

    return towels, patterns


@functools.cache
def count_patterns(pattern: str, towels: tuple[str]) -> int:
    if pattern == "":
        return 1
    return (
        1
        if pattern == ""
        else sum(
            count_patterns(pattern[len(towel) :], towels)
            for towel in towels
            if pattern.startswith(towel)
        )
    )


def main() -> None:
    lines = read_input()
    towels, patterns = parse_input(lines)

    counts = {
        pattern: count
        for pattern in patterns
        if (count := count_patterns(pattern, towels)) != 0
    }

    part_1 = len(counts)
    print(f"{part_1=}")

    part_2 = sum(counts.values())
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day19.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
