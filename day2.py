class ValidationData:
    num1: int
    num2: int
    letter: int

    def __init__(self, min, max, letter):
        self.num1 = min
        self.num2 = max
        self.letter = letter


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        results = []
        lines = f.readlines()
        for line in lines:
            val, letter, password = line.strip().split(' ')
            min, max = val.split('-')
            results.append((ValidationData(int(min), int(max), letter[:-1]), password))
        return results


def is_valid_by_count(min, max, key, password):
    repeats = password.count(key)
    return min <= repeats <= max


def task1():
    passwords = read_data("input2.txt")
    result = 0
    for (valid, password) in passwords:
        if is_valid_by_count(valid.num1, valid.num2, valid.letter, password):
            result += 1
    print(f"Number of valid passwords: {result}")


def is_valid_by_position(pos1, pos2, key, password):
    ind1 = pos1 - 1
    ind2 = pos2 - 1
    if ind1 >= len(password) or ind2 >= len(password):
        return False
    return (password[ind1] == key) != (password[ind2] == key)


def task2():
    passwords = read_data("input2.txt")
    result = 0
    for (valid, password) in passwords:
        if is_valid_by_position(valid.num1, valid.num2, valid.letter, password):
            result += 1
    print(f"Number of valid passwords: {result}")


if __name__ == '__main__':
    task1()
    task2()
