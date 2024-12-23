#!/usr/bin/env python
from collections import defaultdict


def next_secret_number(number: int) -> int:
    number ^= number * 64
    number %= 16777216

    number ^= number // 32
    number %= 16777216

    number ^= number * 2048
    number %= 16777216

    return number


def two_thousandth(number: int) -> int:
    for i in range(2000):
        number = next_secret_number(number)
    return number


def secret_numbers(number: int) -> list[int]:
    out = [number]
    for _ in range(2000):
        number = next_secret_number(number)
        out.append(number)
    return [o % 10 for o in out]


def calc_sequences(starting_number: int) -> dict[tuple[int, int, int, int], int]:
    sequences = {}
    numbers = secret_numbers(starting_number)

    for a, b, c, d, e in list(
        zip(numbers, numbers[1:], numbers[2:], numbers[3:], numbers[4:])
    ):
        sequence = b - a, c - b, d - c, e - d
        value = e

        if sequence not in sequences:
            sequences[sequence] = value
    return sequences


def do_part_2(numbers: list[int]) -> int:
    all_sequences: dict[tuple[int, int, int, int], int] = defaultdict(int)
    for i in numbers:
        sequences = calc_sequences(i)
        for k, v in sequences.items():
            all_sequences[k] += v
    return max(all_sequences.values())


def main() -> None:
    lines = read_input()
    numbers = [int(line) for line in lines]

    part_1 = sum([two_thousandth(i) for i in numbers])
    print(f"{part_1=}")

    part_2 = do_part_2(numbers)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day22.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
