#!/usr/bin/env python
class Schematic:
    def __init__(self, columns):
        self.columns = columns


class Lock(Schematic):
    def __str__(self):
        return f"Key: {self.columns}"


class Key(Schematic):
    def __str__(self):
        return f"Key: {self.columns}"


def parse_schematic(schematic_str: str) -> Schematic:
    columns = tuple(c.count("#") - 1 for c in zip(*schematic_str.split("\n")))
    if schematic_str[0] == "#":
        return Lock(columns)
    else:
        return Key(columns)


def parse_schematics(input_string) -> list[Schematic]:
    return [
        parse_schematic(schematic_lines)
        for schematic_lines in input_string.strip().split("\n\n")
    ]


def check_key(key: Key, lock: Lock) -> bool:
    return all(key + lock < 6 for key, lock in zip(key.columns, lock.columns))


def main() -> None:
    schematics = parse_schematics(read_input())
    locks = [s for s in schematics if isinstance(s, Lock)]
    keys = [s for s in schematics if isinstance(s, Key)]

    part_1 = len([1 for key in keys for lock in locks if check_key(key, lock)])
    print(f"{part_1=}")


def read_input() -> str:
    with open("day25.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
