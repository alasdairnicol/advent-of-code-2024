#!/usr/bin/env python
from collections import Counter


def build_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    a, b = zip(*((int(x) for x in line.split()) for line in lines))
    return sorted(a), sorted(b)


def do_part_1(list_a: list[int], list_b: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(list_a, list_b))


def do_part_2(list_a: list[int], list_b: list[int]) -> int:
    b_counts = Counter(list_b)
    return sum(a * b_counts[a] for a in list_a)


def main() -> None:
    list_a, list_b = build_lists(read_input())

    part_1 = do_part_1(list_a, list_b)
    print(f"{part_1=}")

    part_2 = do_part_2(list_a, list_b)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day01.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
