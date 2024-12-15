#!/usr/bin/env python
from collections import Counter, defaultdict


def next_number(x: int) -> tuple[int, ...]:
    if x == 0:
        return (1,)
    if (xlen := len(str(x))) % 2 == 0:
        return int(str(x)[: xlen // 2]), int(str(x)[xlen // 2 :])
    else:
        return (x * 2024,)


def do_blinks(counts: dict, blinks: int) -> dict:
    for _ in range(blinks):
        new_counts: dict = defaultdict(int)
        for k, count in counts.items():
            for new_k in next_number(k):
                new_counts[new_k] += count
        counts = new_counts
    return counts


def main() -> None:
    input = read_input()
    numbers = [int(x) for x in input.split()]
    counts = Counter(numbers)

    part_1 = sum(do_blinks(counts, 25).values())
    print(f"{part_1=}")

    part_2 = sum(do_blinks(counts, 75).values())
    print(f"{part_2=}")


def read_input() -> str:
    with open("day11.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
