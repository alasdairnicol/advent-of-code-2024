#!/usr/bin/env python
from typing import Literal

Point = tuple[int, int]
Vector = tuple[int, int]
Grid = dict[Point, str]
Instruction = Literal[">", "v", "<", "^"]


def score_grid(grid: Grid) -> int:
    return sum(100 * j + i for (i, j), v in grid.items() if v in "O[")


directions: dict[Instruction, Vector] = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


def make_grid_part_1(lines: list[str]) -> Grid:
    return {
        (i, j): val
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val in "O#"
    }


def make_grid_part_2(lines: list[str]) -> Grid:
    grid = {}
    for j, line in enumerate(lines):
        for i, val in enumerate(line.strip()):
            if val == "#":
                grid[2 * i, j] = "#"
                grid[2 * i + 1, j] = "#"
            elif val == "O":
                grid[2 * i, j] = "["
                grid[2 * i + 1, j] = "]"
    return grid


def find_robot_part_1(lines: list[str]) -> Point:
    return next(
        (i, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val == "@"
    )


def find_robot_part_2(lines: list[str]) -> Point:
    return next(
        (i * 2, j)
        for j, line in enumerate(lines)
        for i, val in enumerate(line.strip())
        if val == "@"
    )


def move_robot_part_1(grid: Grid, robot: Point, instruction: Instruction):
    position = robot
    dx, dy = directions[instruction]
    chain = []
    while True:
        position = position[0] + dx, position[1] + dy
        chain.append(position)
        val = grid.get(position)
        if val != "O":
            break

    if val == "#":
        pass
        # we've hit an obstacle and can't move
    else:
        robot = chain[0]
        if len(chain) > 1:
            grid.pop(chain[0])
            grid[chain[-1]] = "O"

    return robot


def move_robot_part_2(grid: Grid, robot: Point, instruction: Instruction):
    position = robot
    dx, dy = directions[instruction]
    queue = [(robot[0] + dx, robot[1] + dy)]
    to_move = {}
    while queue:
        position = queue.pop(0)
        if position in to_move:
            # already checked
            continue
        val = grid.get(position)
        if val is None:
            continue
        elif val == "#":
            # we've hit an obstacle and can't move
            return robot
        else:
            if dx:
                to_move[position] = val
                queue.append((position[0] + dx, position[1]))
            else:
                to_move[position] = val
                if val == "[":
                    queue.append((position[0], position[1] + dy))
                    # Check the other half of the box
                    queue.append((position[0] + 1, position[1]))
                elif val == "]":
                    # check the next position
                    queue.append((position[0], position[1] + dy))
                    # Check the other half of the box
                    queue.append((position[0] - 1, position[1]))

    # If we've reached here we're allowed to move
    # Deleting all the positions first avoids them being accidentally overwritten later
    for position in to_move:
        del grid[position]
    for position, val in to_move.items():
        grid[position[0] + dx, position[1] + dy] = val

    return robot[0] + dx, robot[1] + dy


def main():
    lines_str, instructions = read_input()
    lines = lines_str.split("\n")

    grid = make_grid_part_1(lines)
    robot = find_robot_part_1(lines)
    instructions = instructions.replace("\n", "")

    for instruction in instructions:
        robot = move_robot_part_1(grid, robot, instruction)

    part_1 = score_grid(grid)
    print(f"{part_1=}")

    grid = make_grid_part_2(lines)
    robot = find_robot_part_2(lines)

    for instruction in instructions:
        robot = move_robot_part_2(grid, robot, instruction)

    part_2 = score_grid(grid)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day15.txt") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
