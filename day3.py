def read_data(filename: str):
    with open(f"input/{filename}") as f:
        results = []
        lines = f.readlines()
        for i, line in enumerate(lines):
            results.append([])
            for letter in line:
                if letter == ".":
                    results[i].append(0)
                elif letter == "#":
                    results[i].append(1)
        return results


def check_trees(forest, di, dj):
    i = 0
    j = 0
    height = len(forest)
    width = len(forest[0])
    sum = 0
    path = []
    while j < height:
        path.append((i, j))
        if forest[j][i] == 1:
            sum += 1
        i = (i + di) % width
        j = j + dj
    return path, sum


def task1():
    forest = read_data("input3.txt")
    path, sum = check_trees(forest, 3, 1)
    print(f"Answer: {sum}")
    print(f"Path is: {path}")


def task2():
    forest = read_data("input3.txt")
    result = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        _, sum = check_trees(forest, slope[0], slope[1])
        result *= sum
    print(f"Answer: {result}")


if __name__ == '__main__':
    task1()
    task2()
