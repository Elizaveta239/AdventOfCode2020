
from typing import Dict


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        bag_info = dict()
        for line in lines:
            info = line.split("bags contain")
            outer = info[0].strip()
            inner = info[1].split(" ")
            child_bags = dict()
            for i, word in enumerate(inner):
                if word.strip().isdigit():
                    color = f"{inner[i + 1]} {inner[i + 2]}"
                    num = int(word)
                    child_bags[color] = num
            bag_info[outer] = child_bags
        return bag_info


def visit_nodes(bags: Dict[str, Dict[str, int]]):
    visited = set()
    gold = "shiny gold"
    next_bags = list()
    for bag, children in bags.items():
        if bag not in visited and gold in children.keys():
            visited.add(bag)
            next_bags.append(bag)
    while len(next_bags) != 0:
        current_bag = next_bags[0]
        next_bags.remove(current_bag)
        for bag, children in bags.items():
            if bag not in visited and current_bag in children.keys():
                visited.add(bag)
                next_bags.append(bag)
    return len(visited)


def task1():
    bags = read_data("input7.txt")
    visited = visit_nodes(bags)
    print(f"Answer is {visited}")


def get_num(bags: Dict[str, Dict[str, int]], color: str):
    if (len(bags[color]) == 0):
        return 0
    res = 0
    for color, num in bags[color].items():
        res = res + num * (get_num(bags, color) + 1)
    return res


def task2():
    bags = read_data("input7.txt")
    visited = get_num(bags, "shiny gold")
    print(f"Answer is {visited}")


if __name__ == "__main__":
    task1()
    task2()
    
