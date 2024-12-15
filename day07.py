#!/usr/bin/env python


def parse_line(line: str) -> tuple[int, list[int]]:
    target, *numbers = [int(x) for x in line.replace(":", "").split()]
    return target, numbers


def is_solvable(
    target: int, numbers: list[int], allow_concatenation: bool = False
) -> bool:
    if numbers[0] > target:
        # Early exit decreases run time by around 33%
        return False
    if len(numbers) == 1:
        return target == numbers[0]
    a, b, *rest = numbers
    if is_solvable(target, [a + b, *rest], allow_concatenation):
        return True
    if is_solvable(target, [a * b, *rest], allow_concatenation):
        return True
    if allow_concatenation and is_solvable(
        target, [int(f"{a}{b}"), *rest], allow_concatenation
    ):
        return True
    return False


def main() -> None:
    lines = read_input()
    equations = [parse_line(line) for line in lines]

    part_1 = sum(
        target
        for target, numbers in equations
        if is_solvable(target, numbers, allow_concatenation=False)
    )
    print(f"{part_1=}")

    part_2 = sum(
        target
        for target, numbers in equations
        if is_solvable(target, numbers, allow_concatenation=True)
    )
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day07.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
