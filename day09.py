#!/usr/bin/env python
from typing import Protocol


class FileSystem(Protocol):
    def defragment(self) -> None:
        pass

    def checksum(self) -> int:
        pass


def expand(input: str) -> list[int | None]:
    expanded: list = []
    for i, val_str in enumerate(input):
        val = int(val_str)
        if i % 2:
            # space
            expanded.extend([None] * val)
        else:
            expanded.extend([i // 2] * val)
    return expanded


class Part1FileSystem:
    def __init__(self, input_str):
        self.blocks = expand(input_str)

    def defragment(self) -> None:
        out = self.blocks[:]
        for i, x in enumerate(out):
            if x is None:
                while (val := out.pop()) is None:
                    continue
                out[i] = val
        self.blocks = out

    def checksum(self) -> int:
        return sum(i * x for i, x in enumerate(self.blocks) if x is not None)


class Part2FileSystem:
    def __init__(self, input_str):
        self.expanded = self.expand(input_str)
        self.files = {
            file_number: (index, length)
            for (index, length, file_number) in self.expanded
            if file_number is not None
        }
        self.empty_spaces = [
            (index, length)
            for (index, length, file_number) in self.expanded
            if file_number is None
        ]

    def expand(self, input: str) -> list[tuple]:
        out = []
        index = 0
        for i, length_str in enumerate(input):
            length = int(length_str)
            file_number = i // 2 if i % 2 == 0 else None
            out.append((index, length, file_number))
            index += length
        return out

    def move_file(self, file_index, file_length, file_number):
        for i, (index, length) in enumerate(self.empty_spaces):
            if index > file_index:
                return
            if length >= file_length:
                self.files[file_number] = (index, file_length)
                self.empty_spaces[i] = (index + file_length, length - file_length)
                return

    def defragment(self) -> None:
        for file_number, (file_index, file_length) in reversed(self.files.items()):
            self.move_file(file_index, file_length, file_number)

    @staticmethod
    def file_checksum(file_index, file_length, file_number) -> int:
        return file_number * sum(range(file_index, file_index + file_length))

    def checksum(self) -> int:
        return sum(
            self.file_checksum(file_index, file_length, file_number)
            for (file_number, (file_index, file_length)) in self.files.items()
        )


def do_part(fs: FileSystem) -> int:
    fs.defragment()
    return fs.checksum()


def main() -> None:
    input_str = read_input()

    part_1 = do_part(Part1FileSystem(input_str))
    print(f"{part_1=}")

    part_2 = do_part(Part2FileSystem(input_str))
    print(f"{part_2=}")


def read_input() -> str:
    with open("day09.txt") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
