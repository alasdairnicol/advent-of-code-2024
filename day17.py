#!/usr/bin/env python


def parse_input(input: str) -> tuple[list[int], list[int]]:
    registers_str, program_str = input.split("\n\n")
    registers = [int(line.split()[-1]) for line in registers_str.split("\n")]
    program = [int(x) for x in program_str.split()[-1].split(",")]
    return registers, program


def combo_operand(registers, value):
    match value:
        case _ if 0 <= value <= 3:
            return value
        case 4:
            return registers[0]
        case 5:
            return registers[1]
        case 6:
            return registers[2]
        case _:
            raise ValueError("Unexpected operand")


class Computer:
    def __init__(self, registers, program):
        self.pointer = 0
        self.registers = registers
        self.program = program
        self.output = []

        self.instructions = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.do_turn()
        except IndexError:
            raise StopIteration

    def do_turn(self):
        instruction = self.instructions[self.program[self.pointer]]
        operand = self.program[self.pointer + 1]
        jump = instruction(operand)
        self.pointer = jump if jump is not None else self.pointer + 2

    def adv(self, operand):
        # calc register A // 2^(combo operand), store in A
        self.registers[0] = self.registers[0] // 2 ** combo_operand(
            self.registers, operand
        )

    def bxl(self, operand):
        # bitwise xor of register B with literal operand
        self.registers[1] ^= operand

    def bst(self, operand):
        # set B to combo operand mod 8
        self.registers[1] = combo_operand(self.registers, operand) % 8

    def jnz(self, operand):
        return None if self.registers[0] == 0 else operand

    def bxc(self, _):
        # bitwise xor of B and C, store in B
        self.registers[1] ^= self.registers[2]

    def out(self, operand):
        self.output.append(combo_operand(self.registers, operand) % 8)

    def bdv(self, operand):
        # calc register A // 2^(combo operand), store in B
        self.registers[1] = self.registers[0] // 2 ** combo_operand(
            self.registers, operand
        )

    def cdv(self, operand):
        # calc register A // 2^(combo operand), store in C
        self.registers[2] = self.registers[0] // 2 ** combo_operand(
            self.registers, operand
        )

    def combo_operand(self, operand):
        match operand:
            case _ if 0 <= operand <= 3:
                return operand
            case 4:
                return self.registers[0]
            case 5:
                return self.registers[1]
            case 6:
                return self.registers[2]
            case _:
                raise ValueError("Unexpected operand")

    @property
    def output_string(self):
        return ",".join(str(o) for o in self.output)


def do_part_1(registers, program) -> str:
    computer = Computer(registers, program)
    for _ in computer:
        pass

    return computer.output_string


def do_part_2(original_registers, program) -> None:
    # I observed that for each additional matching digit,
    # the value of register a increased just over 8x.
    # Therefore we can minimize the number of values to check
    # by multiplying the current guess by 8 each time we match
    # another digit.
    guess = 0

    for n in range(1, len(program) + 1):
        guess *= 8
        wanted = program[-n:]

        while True:
            # if a % 10000000 == 0:
            # print(a)
            registers = original_registers[:]
            registers[0] = guess

            computer = Computer(registers, program)
            for _ in computer:
                pass

            if computer.output[-n:] == wanted:
                break

            guess += 1

    return guess


def main() -> None:
    registers, program = parse_input(read_input())

    part_1 = do_part_1(registers, program)
    print(f"{part_1=}")

    part_2 = do_part_2(registers, program)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day17.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
