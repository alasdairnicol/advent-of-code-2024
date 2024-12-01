#!/usr/bin/env python
from collections import Counter
from typing import Generator


def main():
    lines = read_input()
    lista, listb = zip(*lines)
    lista = sorted(lista)
    listb = sorted(listb)

    b_counts = Counter(listb)

    part_1 = sum(abs(a - b) for a, b in zip(lista, listb))
    part_2 = sum(a * b_counts[a] for a in lista)
    print(f"{part_1=}")
    print(f"{part_2=}")


def read_input() -> Generator[list[int], None, None]:
    with open("day01.txt") as f:
        return ([int(x) for x in line.split()] for line in f.readlines())


if __name__ == "__main__":
    main()
