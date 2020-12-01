from typing import List, Tuple

CRAZY_YEAR = 2020


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        return list(map(lambda x: int(x), lines))


def find_two_numbers(numbers: List[int], sum: int, first_index: int = 0) -> Tuple[int, int]:
    n = len(numbers)
    for i in range(first_index, n):
        for j in range(i + 1, n):
            first = numbers[i]
            second = numbers[j]
            if first + second == sum:
                return first, second


def find_three_numbers(numbers: List[int], sum: int) -> Tuple[int, int, int]:
    n = len(numbers)
    for i in range(0, n):
        if res := find_two_numbers(numbers, sum - numbers[i], i + 1):
            return numbers[i], res[0], res[1]


def task1():
    numbers = read_data("input1.txt")
    first, second = find_two_numbers(numbers, CRAZY_YEAR)
    print(f"Task 1: Numbers are {first}, {second}, Sum = {first + second}")
    print(f"Answer is {first * second}")


def task2():
    numbers = read_data("input1.txt")
    first, second, third = find_three_numbers(numbers, CRAZY_YEAR)
    print(f"Task 2: Numbers are {first}, {second}, {third}, Sum = {first + second + third}")
    print(f"Answer is {first * second * third}")


if __name__ == "__main__":
    task1()
    task2()
