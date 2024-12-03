#!/usr/bin/env python
import re


def do_part_1(line: str) -> int:
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", line))


def do_part_2(line: str) -> int:
    instructions = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line)

    total = 0
    enabled = True
    for instruction, x, y in instructions:
        if instruction == "don't()":
            enabled = False
        elif instruction == "do()":
            enabled = True
        elif enabled:
            total += int(x) * int(y)

    return total


def main():
    line = read_input()
    part_1 = do_part_1(line)
    print(f"{part_1=}")

    part_2 = do_part_2(line)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day03.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
