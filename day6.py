from typing import List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.read()
        lines = lines.split("\n\n")
        groups = []
        for group in lines:
            person = group.split("\n")
            clean_person = list(filter(lambda p: p != "", person))
            groups.append(clean_person)
        return groups


def get_any_answer_for_group(group: List[str]):
    answers = set()
    for person in group:
        answers |= set(person)
    return answers


def task1():
    groups = read_data("input6.txt")
    sum = 0
    for group in groups:
        sum += len(get_any_answer_for_group(group))
    print(f"Answer is {sum}")


def get_every_answer_for_group(group: List[str]):
    answers = set(group[0])
    for person in group:
        answers &= set(person)
    return answers


def task2():
    groups = read_data("input6.txt")
    sum = 0
    for group in groups:
        sum += len(get_every_answer_for_group(group))
    print(f"Answer is {sum}")


if __name__ == "__main__":
    task1()
    task2()
