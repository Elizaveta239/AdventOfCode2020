from typing import Tuple, List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        commands = list()
        for com in lines:
            items = com.split(" ")
            commands.append((items[0], int(items[1])))
        return commands


def acc_before_loop(commands: List[Tuple[str, int]]):
    visited = [False for _ in range(len(commands))]
    i = 0
    acc = 0
    while not visited[i]:
        visited[i] = True
        comm, offset = commands[i]
        if comm == "acc":
            acc += offset
            i += 1
        elif comm == "jmp":
            i += offset
        elif comm == "nop":
            i += 1
        else:
            raise ValueError("Wrong instruction")
    return acc


def task1():
    commands = read_data("input8.txt")
    acc = acc_before_loop(commands)
    print(f"Answer is {acc}")


def acc_if_path_exist(commands: List[Tuple[str, int]]):
    visited = [False for _ in range(len(commands))]
    i = 0
    acc = 0
    while i != len(commands):
        if i < 0 or i >= len(visited):
            return -1
        if visited[i]:
            return -1
        visited[i] = True
        comm, offset = commands[i]
        if comm == "acc":
            acc += offset
            i += 1
        elif comm == "jmp":
            i += offset
        elif comm == "nop":
            i += 1
        else:
            raise ValueError("Wrong instruction")
    if i > 0:
        return acc
    else:
        return i


def try_combinations(commands: List[Tuple[str, int]]):
    for i in range(len(commands)):
        comm, offset = commands[i]
        fixed_commands = commands[:]
        if comm == "nop":
            fixed_commands[i] = ("jmp", offset)
        elif comm == "jmp":
            fixed_commands[i] = ("nop", offset)
        acc = acc_if_path_exist(fixed_commands)
        if acc > 0:
            return acc


def task2():
    commands = read_data("input8.txt")
    acc = try_combinations(commands)
    print(f"Accumulator value {acc}")


if __name__ == '__main__':
    task1()
    task2()
