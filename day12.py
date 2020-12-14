from math import radians, cos, sin
from typing import List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        return list(map(lambda x: x[:-1], lines))


def move_ship(pos: List[float], action: str):
    val = int(action[1:])
    if action.startswith("N"):
        pos[1] += val
    elif action.startswith("S"):
        pos[1] -= val
    elif action.startswith("E"):
        pos[0] += val
    elif action.startswith("W"):
        pos[0] -= val
    elif action.startswith("R"):
        pos[2] = pos[2] - val
    elif action.startswith("L"):
        pos[2] = pos[2] + val
    elif action.startswith("F"):
        nex_x = pos[0] + cos(radians(pos[2])) * val
        nex_y = pos[1] + sin(radians(pos[2])) * val
        pos[0] = nex_x
        pos[1] = nex_y


def follow_path(path: List[str]):
    pos = [0.0, 0.0, 0.0]
    for action in path:
        move_ship(pos, action)
    return pos


def task1():
    path = read_data("input12.txt")
    ans = follow_path(path)
    print(abs(ans[0]) + abs(ans[1]))


def move_ship2(ship: List[float], mp: List[float], action: str):
    val = int(action[1:])
    if action.startswith("N"):
        mp[1] += val
    elif action.startswith("S"):
        mp[1] -= val
    elif action.startswith("E"):
        mp[0] += val
    elif action.startswith("W"):
        mp[0] -= val
    elif action.startswith("R"):
        rad = radians(val * (-1))
        x = mp[0]
        y = mp[1]
        x_new = x * cos(rad) - y * sin(rad)
        y_new = y * cos(rad) + x * sin(rad)
        mp[0] = x_new
        mp[1] = y_new
    elif action.startswith("L"):
        rad = radians(val)
        x = mp[0]
        y = mp[1]
        x_new = x * cos(rad) - y * sin(rad)
        y_new = y * cos(rad) + x * sin(rad)
        mp[0] = x_new
        mp[1] = y_new
    elif action.startswith("F"):
        ship[0] = ship[0] + mp[0] * val
        ship[1] = ship[1] + mp[1] * val


def follow_path2(path: List[str]):
    ship = [0.0, 0.0]
    mp = [10.0, 1.0]
    for action in path:
        move_ship2(ship, mp, action)
    return ship


def task2():
    path = read_data("input12.txt")
    ans = follow_path2(path)
    # print(ans)
    print(abs(ans[0]) + abs(ans[1]))


if __name__ == "__main__":
    task1()
    task2()
