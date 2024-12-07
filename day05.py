#!/usr/bin/env python
from collections import defaultdict

Rules = dict[int, list[int]]
Update = list[int]


def make_rules(rules_lines: list[str]) -> Rules:
    rules = defaultdict(list)
    for line in rules_lines:
        before, after = line.split("|")
        rules[int(before)].append(int(after))
    return rules


def make_updates(updates_str: list[str]) -> list[Update]:
    return [[int(x) for x in line.split(",")] for line in updates_str]


def check_update(rules: Rules, update: Update) -> bool:
    if len(update) == 1:
        return True
    head, *update = update
    if any(head in rules.get(u, []) for u in update):
        return False
    else:
        return check_update(rules, update)


def fix_order(rules: Rules, update: Update) -> Update:
    update = update[:]
    while not check_update(rules, update):
        for i in range(len(update) - 1):
            if update[i] in rules[update[i + 1]]:
                # print("Swapping", update[i + 1], update[i])
                update[i : i + 2] = update[i + 1], update[i]
    return update


def do_part_1(rules: Rules, updates: list[Update]) -> int:
    correct = [u for u in updates if check_update(rules, u)]
    return sum(u[len(u) // 2] for u in correct)


def do_part_2(rules: Rules, updates: list[Update]) -> int:
    return sum(
        fix_order(rules, u)[len(u) // 2] for u in updates if not check_update(rules, u)
    )


def main():
    rules_str, updates_str = read_input()

    rules = make_rules(rules_str.split("\n"))
    updates = make_updates(updates_str.split("\n"))

    part_1 = do_part_1(rules, updates)
    print(f"{part_1=}")

    part_2 = do_part_2(rules, updates)
    print(f"{part_2=}")


def read_input() -> tuple[str, str]:
    with open("day05.txt") as f:
        rules_str, updates_str = f.read().strip().split("\n\n", maxsplit=1)
        return rules_str, updates_str


if __name__ == "__main__":
    main()
