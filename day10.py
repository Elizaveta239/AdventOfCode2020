from typing import List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        nums = map(lambda x: int(x.strip()), lines)
        return list(nums)


def find_diffs(adapters, path):
    count1 = 0
    count3 = 0
    for i in range(0, len(path) - 1):
        if adapters[path[i + 1]] - adapters[path[i]] == 1:
            count1 += 1
        if adapters[path[i + 1]] - adapters[path[i]] == 3:
            count3 += 1
    return count1 * count3


def task1():
    adapters = read_data("input10.txt")
    adapters.append(0)
    adapters = sorted(adapters)
    p = [i for i in range(0, len(adapters))]
    adapters.append(max(adapters) + 3)
    p.append(len(adapters) - 1)
    print(find_diffs(adapters, p))


def count(adapters: List[int]):
    n = len(adapters)
    ways = [0 for _ in range(0, n)]
    ways[0] = 1
    for ind in range(1, n):
        for j in range(1, 4):
            if (ind - j >= 0) and (adapters[ind] - adapters[ind - j] <= 3):
                ways[ind] += ways[ind - j]
    return ways[n - 1]


def task2():
    adapters = read_data("input10.txt")
    adapters.append(0)
    adapters = sorted(adapters)
    print(count(adapters))


if __name__ == "__main__":
    task1()
    task2()
