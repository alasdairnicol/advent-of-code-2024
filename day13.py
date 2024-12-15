#!/usr/bin/env python
Vector = tuple[int, int]
Machine = tuple[Vector, Vector, Vector]


def parse_machine(machine_str: str) -> Machine:
    linea, lineb, linec = machine_str.strip().split("\n")
    words_a = linea.split()
    words_b = lineb.split()
    words_c = linec.split()
    da = (int(words_a[2][2:-1]), int(words_a[3][2:]))
    db = (int(words_b[2][2:-1]), int(words_b[3][2:]))
    target = (int(words_c[1][2:-1]), int(words_c[2][2:]))
    return da, db, target


def solve_machine(da: Vector, db: Vector, target: Vector) -> int:
    b, rem = divmod(
        (da[0] * target[1] - da[1] * target[0]), (da[0] * db[1] - da[1] * db[0])
    )
    if rem:
        return 0
    a, rem = divmod(target[0] - db[0] * b, da[0])
    if rem:
        return 0
    return 3 * a + b


def total_presses(machines: list[Machine], offset: int = 0) -> int:
    total = 0
    for da, db, target in machines:
        target = target[0] + offset, target[1] + offset
        total += solve_machine(da, db, target)
    return total


def main() -> None:
    machine_strings = read_input()
    machines = [parse_machine(machine_str) for machine_str in machine_strings]

    part_1 = total_presses(machines)
    print(f"{part_1=}")

    part_2 = total_presses(machines, offset=10000000000000)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day13.txt") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
