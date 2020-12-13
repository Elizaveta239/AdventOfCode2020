from typing import List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        map = []
        for line in lines:
            seats = []
            for c in line.strip():
                seats.append(c)
            map.append(seats)
        return map


def get_adj(i, j, n, m):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            if 0 <= i + di < n and 0 <= j + dj < m:
                yield i + di, j + dj


def copy(map):
    res = []
    for i in range(len(map)):
        res.append(map[i][:])
    return res


def apply_rule(map: List[List[str]]):
    n = len(map)
    res = copy(map)
    for i in range(0, n):
        m = len(map[i])
        for j in range(0, m):
            if map[i][j] == ".":
                continue
            elif map[i][j] == "L":
                for (ni, nj) in get_adj(i, j, n, m):
                    if map[ni][nj] == "#":
                        break
                else:
                    res[i][j] = "#"
            elif map[i][j] == "#":
                occ = 0
                for (ni, nj) in get_adj(i, j, n, m):
                    if map[ni][nj] == "#":
                        occ += 1
                if occ >= 4:
                    res[i][j] = "L"
    return res


def equals(map, res):
    n = len(map)
    for i in range(0, n):
        m = len(map[i])
        for j in range(0, m):
            if map[i][j] != res[i][j]:
                return False
    return True


def check(map: List[List[str]]):
    res = apply_rule(map)
    while not equals(map, res):
        map = copy(res)
        res = apply_rule(map)
    return res


def count_occ(map):
    occ = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == "#":
                occ += 1
    return occ


def task1():
    map = read_data("input11.txt")
    res = check(map)
    print(count_occ(res))


def apply_rule2(map: List[List[str]]):
    n = len(map)
    res = copy(map)
    for i in range(0, n):
        m = len(map[i])
        for j in range(0, m):
            if map[i][j] == ".":
                continue
            elif map[i][j] == "L":
                for (ni, nj) in get_adj2(map, i, j, n, m):
                    if map[ni][nj] == "#":
                        break
                else:
                    res[i][j] = "#"
            elif map[i][j] == "#":
                occ = 0
                for (ni, nj) in get_adj2(map, i, j, n, m):
                    if map[ni][nj] == "#":
                        occ += 1
                if occ >= 5:
                    res[i][j] = "L"
    return res


def get_next(map, i, j, n, m, diff):
    di = 0
    dj = 0
    while 0 <= i + di < n and 0 <= j + dj < m:
        if di == 0 and dj == 0:
            di += diff[0]
            dj += diff[1]
            continue
        if map[i + di][j + dj] != '.':
            return i + di, j + dj
        di += diff[0]
        dj += diff[1]


def get_adj2(map, i, j, n, m):
    for diff_i in range(-1, 2):
        for diff_j in range(-1, 2):
            if diff_i == 0 and diff_j == 0:
                continue
            res = get_next(map, i, j, n, m, (diff_i, diff_j))
            if res is not None:
                yield res


def check2(map: List[List[str]]):
    res = apply_rule2(map)
    while not equals(map, res):
        map = copy(res)
        res = apply_rule2(map)
    return res


def task2():
    map = read_data("input11.txt")
    res = check2(map)
    # for i in range(len(res)):
    #     print(res[i])
    print(count_occ(res))


if __name__ == "__main__":
    task1()
    task2()
